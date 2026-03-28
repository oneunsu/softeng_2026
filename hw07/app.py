from flask import Flask, abort, render_template

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="")

ALLOWED_PAGES = {"index", "about", "projects", "vision"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<page>.html")
def render_page(page):
    if page not in ALLOWED_PAGES:
        abort(404)
    return render_template(f"{page}.html")

if __name__ == "__main__":
    app.run(debug=True)