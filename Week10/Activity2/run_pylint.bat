
@echo off
where pylint >NUL 2>&1
if ERRORLEVEL 1 (
  echo Please: pip install pylint
  exit /b 1
)
pylint src/oo_analyzer tests --fail-under=9.5 | tee pylint_report.txt
