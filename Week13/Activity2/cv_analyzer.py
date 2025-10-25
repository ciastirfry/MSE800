# cv_analyzer.py
# One-file CV analyzer using Google Gemini (google-genai).
# - Reads a .docx CV from a given path
# - Sends a single-string prompt to Gemini
# - Prints a concise HR-style summary + recommendations
#
# Run:
#   python cv_analyzer.py.py --cv "C:\path\to\YourCV.docx" - 

import os
import argparse
from pathlib import Path

# Optional: .env support (GEMINI_API_KEY in a .env file)
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Document reader
try:
    import docx  # python-docx
except Exception as e:
    raise SystemExit("Missing dependency 'python-docx'. Install: pip install python-docx") from e

# Gemini SDK
try:
    from google import genai
except Exception as e:
    raise SystemExit("Missing dependency 'google-genai'. Install: pip install google-genai") from e


def read_docx_text(docx_path: Path) -> str:
    if not docx_path.exists():
        raise FileNotFoundError(f"File not found: {docx_path}")
    document = docx.Document(str(docx_path))
    paragraphs = [p.text for p in document.paragraphs]
    text = "\n".join(paragraphs).strip()
    if not text:
        raise ValueError("The .docx file appears to have no readable text.")
    return text


def build_prompt(cv_text: str) -> str:
    return f"""
You are an experienced Tech Talent Partner. Analyze the CV below and produce a clear, skimmable brief for a time-poor hiring manager in NZ tech (DevOps/Cloud/SRE/Platform focus).

CV TEXT:
{cv_text}

---
DELIVERABLE (write directly, no placeholders):
1) Candidate Snapshot
   - Full name (if present)
   - Contact info found (email/phone/LinkedIn)
   - One-paragraph executive summary (seniority, value proposition)

2) Experience Highlights
   - Total years (approx.)
   - Most recent role (title, company)
   - 3–5 impact bullets (quantify where possible)

3) Skills Matrix
   - Technical: 5–8 key tools/clouds/frameworks
   - Soft skills: 3–5 relevant traits

4) NZ Market Fit
   - Keywords likely valued by NZ recruiters (Seek/LinkedIn style)
   - Quick ATS polish tips (formatting, dates, consistency)

5) Risks / Red Flags (if any)
   - Note gaps, job hopping, vague achievements (or say 'None significant')

6) Next Actions (checklist)
   - 5–8 actionable edits the candidate should do next
"""


def main():
    parser = argparse.ArgumentParser(description="Analyze a .docx CV with Gemini and print an HR-style summary.")
    parser.add_argument("--cv", required=True, help="Path to .docx CV")
    parser.add_argument("--model", default=os.getenv("MODEL_ID", "gemini-2.5-flash"),
                        help="Gemini model ID (default: gemini-2.5-flash)")
    parser.add_argument("--save", default=None, help="Optional path to save the output (e.g., outputs\\cv_report.md)")
    args = parser.parse_args()

    # Read API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit(
            "GEMINI_API_KEY not set. Set it in your environment or a .env file.\n"
            "Example (PowerShell): setx GEMINI_API_KEY \"your-key-here\"  (then open a new terminal)"
        )

    # Read CV text
    cv_path = Path(args.cv)
    cv_text = read_docx_text(cv_path)

    # Build prompt
    prompt = build_prompt(cv_text)

    # Call Gemini (pass a single string to 'contents')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=args.model,
        contents=prompt
    )

    # Extract text
    output_text = getattr(response, "text", None) or getattr(response, "output_text", None) or str(response)

    # Print to console
    print("\n===== CV REVIEW =====\n")
    print(output_text)
    print("\n=====================\n")

    # Optionally save to file
    if args.save:
        out_path = Path(args.save)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text, encoding="utf-8")
        print(f"Saved report to: {out_path.resolve()}")


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Error: {ex}")
