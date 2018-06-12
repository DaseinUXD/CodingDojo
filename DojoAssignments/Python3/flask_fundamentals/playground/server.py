from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    print("at index")
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html')

if __name__ == '__main__':
    app.run()
