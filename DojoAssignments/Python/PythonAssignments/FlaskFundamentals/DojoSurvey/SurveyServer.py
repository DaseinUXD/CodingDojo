from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'this is the secret key'


# landing page
@app.route('/')
def index():
    return render_template('index.html')


# results page
@app.route('/result', methods=['GET','POST'])
def result():
    # name = session['name']

    return render_template('result.html')


@app.route('/submit', methods=['POST'])
def submit():
    # return "Hello"
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/result')


if __name__ == '__main__':
    app.run()
