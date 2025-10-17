# Week 12 – Activity 2: Flask Web App (Hyperlink + Image)

This app lets an **end user**:
1) Enter a **hyperlink (text + URL)**, and
2) Provide an **image** either by **URL** or by **file upload**.

The result page shows the clickable link and the image.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000/
```

## Notes
- Allowed file types: png, jpg, jpeg, gif, webp
- Max upload size: 5 MB
- Uploaded files are stored in `static/uploads/`

