
from __future__ import annotations
import argparse
import json
from .inputs import InputData
from .processor import Processor
from .analyzers import LengthAnalyzer, UppercaseAnalyzer

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OO Analyzer: length and uppercase counts.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--string", type=str, help="A single string to analyze.")
    group.add_argument("--list", type=str, help='A JSON array of strings, e.g. \'["Hi","NZ"]\'')
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.string is not None:
        data = InputData(args.string)
    else:
        try:
            parsed = json.loads(args.list)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"List must be valid JSON: {exc}") from exc
        data = InputData(parsed)

    processor = Processor([LengthAnalyzer(), UppercaseAnalyzer()])
    metrics = processor.run(data)
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
