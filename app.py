from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    


if __name__=="__main__":
    app.run(debug=True)