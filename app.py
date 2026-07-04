from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = "Some data"
    return data

@app.route("/cards/")
def cards():
    return render_template("cards.html")

# 127.0.0.1/ - address

if __name__ == "__main__":
    app.run(debug=True)
