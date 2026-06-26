from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

l=[]
@app.route("/home",methods=["POST","GET"])
def home():
    
    if request.method == "POST":
        todo = request.form.get("todo")
        if todo:
            l.append(todo)
    return render_template("home.html", todos=l)

if __name__ == "__main__":
    app.run(debug=True)

