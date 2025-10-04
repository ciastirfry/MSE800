
#!/usr/bin/env bash
set -euo pipefail
if ! command -v pylint >/dev/null 2>&1; then
  echo "Please: pip install pylint" >&2
  exit 1
fi
pylint src/oo_analyzer tests --fail-under=9.5 | tee pylint_report.txt
