from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/hairdresser")
def hairdresser():
    return render_template("/portfolio/hairdresser.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("/portfolio/boogle.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("/portfolio/fakebook.html")

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
