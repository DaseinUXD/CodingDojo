from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/blue')
def blue():
    return render_template("blue.html")

@app.route('/orange')
def orange():
    return render_template("orange.html")

@app.route('/red')
def red():
    return render_template("red.html")

@app.route('/purple')
def purple():
    return render_template("purple.html")

@app.route('/error')
def error():
    return render_template("error.html")



if __name__ == '__main__':
    app.run()
