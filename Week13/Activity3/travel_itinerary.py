"""
AI-Powered Travel Itinerary Generator (Gemini, Teen Edition)
Adds positive/negative prompt engineering knobs.
Author: Fred
"""

import os
import json
import argparse
import google.generativeai as genai

# -------------------------
# Gemini setup
# -------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("Please set GEMINI_API_KEY environment variable.")

# Prefer latest aliases to avoid 404s on older endpoints
MODEL_NAME = "gemini-1.5-flash-latest"

genai.configure(api_key=API_KEY)

# -------------------------
# Prompt ingredients
# -------------------------
POSITIVE_GUIDANCE_DEFAULT = """
Audience: teenagers (13–19). 
Prioritize: budget-friendly options, outdoor adventures, social but supervised activities, walkable/public-transport routes, and hands-on experiences (workshops, tours, sports).
Add realistic timing windows (e.g., 09:00–12:00 / 13:00–17:00 / 17:30–20:30).
Include 1–2 affordable local food picks per day (e.g., food courts, student spots, street food).
Include getting-around notes (bus/ferry/day-pass suggestions) without asserting uncertain facts.
Add short safety notes where relevant (meet-up points, daylight routes); suggest reasonable curfew (back by ~21:00).
"""

NEGATIVE_CONSTRAINTS_DEFAULT = """
Do NOT include: bars, nightclubs, alcohol, 18+/21+ venues, gambling, unsafe or unsupervised high-risk activities, or generic filler like "Enjoy your trip."
Avoid luxury-only items (helicopters, private jets, ultra-expensive spas/resorts).
No vague claims or made-up details; when uncertain, suggest how to verify locally.
"""

JSON_SCHEMA_HINT = """
Respond ONLY in valid JSON (UTF-8, no trailing commas).
Use this exact schema (array length == {days}):
[
  {{
    "day": 1,
    "location": "{destination}",
    "activities": [
      "Morning (09:00–12:00): ... (safety: ...)",
      "Afternoon (13:00–17:00): ... (getting around: ...)",
      "Evening (17:30–20:30): ... (curfew aim: back by 21:00)"
    ],
    "estimated_cost": 0
  }}
]
Keys must be exactly: day, location, activities, estimated_cost.
estimated_cost is a NUMBER only (no currency symbol).
"""

MARKDOWN_FORMAT_HINT = """
Format the answer in clean Markdown with:
- A title and 1-paragraph summary
- "Budget Overview" (bullets)
- Day sections (Day 1..{days}) with:
  - Morning / Afternoon / Evening
  - 1–2 Meal picks (cheap/moderate)
  - Getting around
  - Estimated daily spend (number + currency code, e.g., "60 NZD")
- A short "Safety & Tips" section at the end
"""


def build_prompt(destination: str,
                 days: int,
                 budget: str,
                 interests: list[str],
                 output_format: str,
                 positive_guidance: str = POSITIVE_GUIDANCE_DEFAULT,
                 negative_constraints: str = NEGATIVE_CONSTRAINTS_DEFAULT) -> str:
    """Create a teen-focused prompt with explicit positive/negative guidance."""
    header = f"""
You are a professional teen travel planner.

Create a detailed {days}-day itinerary for {destination} for teens aged 13–19.
Daily budget target: {budget}.
Traveler interests: {', '.join(interests) if interests else 'general sightseeing'}.
"""
    body = f"""
Follow these POSITIVE guidelines:
{positive_guidance.strip()}

Follow these NEGATIVE constraints:
{negative_constraints.strip()}
"""

    if output_format == "json":
        tail = JSON_SCHEMA_HINT.format(days=days, destination=destination)
    else:
        tail = MARKDOWN_FORMAT_HINT.format(days=days)

    return header + body + tail


def generate_itinerary(destination: str, days: int, budget: str, interests: list[str], output_format: str):
    """Call Gemini and (optionally) parse JSON."""
    prompt = build_prompt(destination, days, budget, interests, output_format)

    model = genai.GenerativeModel(
        MODEL_NAME,
        system_instruction=(
            "You are a helpful AI travel assistant. When asked for JSON, output strictly valid JSON only; "
            "otherwise, return clean Markdown."
        )
    )

    resp = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            temperature=0.7,
            max_output_tokens=1400,
        ),
    )
    text = (getattr(resp, "text", "") or "").strip()

    if output_format == "json":
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Try to grab largest JSON block if model added extra text
            import re
            blocks = re.findall(r"\[.*\]", text, flags=re.DOTALL)
            if blocks:
                try:
                    return json.loads(blocks[0])
                except json.JSONDecodeError:
                    pass
    return text  # Markdown (or raw text fallback)


def main():
    parser = argparse.ArgumentParser(description="Teen-focused travel itinerary generator (Gemini).")
    parser.add_argument("--destination", required=False, help="City/region, e.g. 'Queenstown, NZ'")
    parser.add_argument("--days", type=int, required=False, default=4, help="Number of days (default: 4)")
    parser.add_argument("--budget", required=False, default="60", help="Daily budget number (e.g., 60)")
    parser.add_argument("--interests", nargs="*", default=["hiking", "views", "street food"],
                        help="Interests (space-separated). Example: --interests beaches museums photography")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output format (markdown|json). Default: markdown")
    args = parser.parse_args()

    # Interactive fallback if not provided via flags
    destination = args.destination or input("Enter destination: ").strip()
    if not args.destination:
        try:
            args.days = int(input("Number of days: ").strip() or args.days)
        except ValueError:
            pass
        args.budget = input("Daily budget number (e.g. 60): ").strip() or args.budget
        raw = input("Interests (comma-separated, optional): ").strip()
        if raw:
            args.interests = [x.strip() for x in raw.split(",") if x.strip()]

    print("\nGenerating your teen-friendly itinerary...\n")
    result = generate_itinerary(destination, args.days, args.budget, args.interests, args.format)

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result)


if __name__ == "__main__":
    main()
