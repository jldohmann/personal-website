from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about")
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/gratitude")
@app.route("/gratitude.html")
def gratitude():
    return render_template("gratitude.html")

@app.route("/resume")
@app.route("/resume.html")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)