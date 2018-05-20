from flask import Flask, session, request, redirect, render_template
import random
app = Flask(__name__)

app.secret_key="this is the key"

app.guess = random.randrange(0, 101)

app.decision = ''

@app.route('/')
def index():
    print(app.guess)
    # session['decision'] = app.decision

    # session['request'] = session.clear
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # session['decision'] = None
    session['number'] = app.guess
    session['guess'] = request.form['number_guessed']
    print(session['guess'] + " was guessed")
    print(type(app.guess))
    print(type(['guess']))
    print(type(request.form['number_guessed']))
    guess = session['guess']
    guessInt = int(guess)
    session['decision']=''
    if guessInt > app.guess:
        print('greater')
        session['decision'] = 'greater'
        # return redirect('/greater')
    elif guessInt < app.guess:
        print('less')
        session['decision'] = 'less'
        # return redirect('/less')
    elif guessInt == app.guess:
        print('matched')
        session['decision'] = 'matched'
    else:
        session['decision'] = None
    print(type(int(guess)))
    print ('i submitted')
    return redirect('/')

# @app.route('/greater')
# def greater():
#     return


if __name__ == '__main__':
    app.run(debug=True)
