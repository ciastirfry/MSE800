
# Week 10 - Activity 2: OO Analyzer (Extended) + Pylint

Extends Activity 1 by adding **digit** and **special character** counts.

**Metrics**
- `total_length`     — string: characters; list: items
- `uppercase_chars`  — A–Z across string/list
- `digits`           — 0–9 across string/list
- `special_chars`    — non-alphanumeric & non-whitespace characters

## Run
python -m oo_analyzer.main --string "Hello NZ 2025! @Yoobee#"
python -m oo_analyzer.main --list '["Hi!","NZ-2025","Yoobee :)"]'

## Pylint report
Linux/macOS:  bash run_pylint.sh
Windows:       run_pylint.bat

Report saved to: pylint_report.txt
