from flask import Flask, redirect, request, session, render_template
import random
app = Flask(__name__)

app.secret_key='the secret is safe with me'
app.guess = random.randrange(0,101)


@app.route('/')
def index():
    session['guess'] = 0
    session['number'] = random.randrange(0,101)
    return render_template('index.html', guess=int(session['guess']), number = int(session['number']))

@app.route('/submit', methods=['POST'])
def submit():
    session['number'] = app.guess
    number=int(session['number'])
    session['guess'] = request.form['number_guessed']
    guess = int(session['guess'])
    if guess < number:
        print(guess)
        print(number)

    return redirect('/')

if __name__ == '__main__':
    app.run()
