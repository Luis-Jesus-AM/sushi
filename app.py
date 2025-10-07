from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index ():
    arr = ["luis", "pedro", "becerro ", "pepito"]
    autor = "Luis jesus Antonio Marin "
    return render_template("index.html", nombre= autor, amigos = arr)

if __name__ == "__main__":
    app.run(debug=True)