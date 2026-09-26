from flask import Flask, render_template, request

app = Flask(__name__)

notes = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/notes", methods=["GET", "POST"])
def notes_page():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]

        notes[title] = text

    return render_template("notes.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)