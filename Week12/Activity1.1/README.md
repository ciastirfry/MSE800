# Week 12 – Activity 1.1: Flask – Variable Path

A tiny Flask app demonstrating a variable path like `/username/Lili` that renders **“Lili is learning Flask!”**

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:5000/
```
- Try the form on `/` or directly visit `http://127.0.0.1:5000/username/Lili`

## Push to GitHub

```bash
git init
git add .
git commit -m "Week 12 – Activity 1.1: Flask variable path demo"
git branch -M main
git remote add origin https://github.com/<your-username>/week12-flask-variable-path.git
git push -u origin main
```
