from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/go", methods=["POST"])
def go():
    name = request.form.get("name", "").strip()
    if not name:
        return redirect(url_for("home"))
    return redirect(url_for("username", name=name))

@app.route("/username/<name>")
def username(name):
    return render_template("username.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
