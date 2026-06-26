from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []


@app.route("/")
def index():
    return render_template("index.html", notes=notes)

@app.route("/add_note", methods=["POST"])
def add_note():
    title = request.form["title"]
    content = request.form["content"]
    notes.append({"title": title, "content": content})
    return redirect("/")

@app.route("/delete_note/<int:index>", methods=["POST"])
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)   # remove the note at that position
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)