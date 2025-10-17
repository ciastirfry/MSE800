import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/build", methods=["POST"])
def build():
    link_text = request.form.get("link_text", "").strip()
    link_url = request.form.get("link_url", "").strip()
    img_url = request.form.get("img_url", "").strip()

    if img_url and (img_url.startswith("http://") or img_url.startswith("https://")):
        image_src = img_url
    else:
        file = request.files.get("image_file")
        if file and file.filename:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                base, ext = os.path.splitext(filename)
                i = 1
                while os.path.exists(save_path):
                    filename = f"{base}_{i}{ext}"
                    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                    i += 1
                file.save(save_path)
                image_src = url_for("static", filename=f"uploads/{filename}")
            else:
                flash("Unsupported file type. Use: png, jpg, jpeg, gif, webp", "error")
                return redirect(url_for("index"))
        else:
            flash("Provide an Image URL or upload a file.", "error")
            return redirect(url_for("index"))

    if not link_url or not (link_url.startswith("http://") or link_url.startswith("https://")):
        flash("Please provide a valid hyperlink URL (must start with http/https).", "error")
        return redirect(url_for("index"))

    if not link_text:
        link_text = link_url

    return render_template("result.html", link_text=link_text, link_url=link_url, image_src=image_src)

if __name__ == "__main__":
    app.run(debug=True)
