from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/ani")
def ani ():
    return render_template("ani.html")

@app.route("/vei")
def vei ():
    return render_template("vei.html")

@app.route("/mun")
def mun ():
    return render_template("mun.html")

@app.route("/ace")
def ace ():
    return render_template("ace.html")

if __name__ == "__main__":
    app.run(debug=True)
