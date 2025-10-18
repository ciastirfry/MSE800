
# Week 12 - Activity 5 : Initial Web- APP with Django

A tiny Django project with **no app**. One route at `/welcome/<name>/` returns a simple greeting.

## Run

```bash
python -m venv .venv
# Windows PowerShell:  . .\.venv\Scripts\Activate.ps1
# macOS/Linux:         source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```
Open: http://127.0.0.1:8000/welcome/Fred/
