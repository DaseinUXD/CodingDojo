from flask import Flask, session, redirect, render_template
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')
def submit():

    return redirect()


if __name__ == '__main__':
    app.run()
