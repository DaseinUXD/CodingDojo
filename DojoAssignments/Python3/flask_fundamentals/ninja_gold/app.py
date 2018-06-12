from flask import Flask, session, request, render_template, redirect
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = "just between you and me"

app.gold = 0

@app.route('/')
def index():
    # print(session['gold'])
    session['gold'] = app.gold
    gold = session['gold']

    return render_template('index.html', gold = gold)


@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    if request.form['location'] == 'farm':
        au_farm = random.randrange(10, 20)
        print(au_farm)
        app.gold = app.gold + int(au_farm)
        print('farm')
        activity = "Earned {} gold from the {}! ({})".format(app.gold, request.form['location'], datetime.datetime.now())
        session['activity']=activity
        print(activity)


    if request.form['location'] == 'cave':
        au_cave = random.randrange(5, 10)
        print(au_cave)
        app.gold = app.gold + int(au_cave)
        print('cave')
        activity = "Earned {} gold from the {}! ({})".format(app.gold, request.form['location'], datetime.datetime.now())
        session['activity']=activity
        print(activity)

    if request.form['location'] == 'house':
        au_house = random.randrange(2, 5)
        print(au_house)
        app.gold = app.gold + int(au_house)
        print('house')
        activity = "Earned {} gold from the {}! ({})".format(app.gold, request.form['location'], datetime.datetime.now())
        session['activity'] = activity
        print(activity)

    if request.form['location'] == 'casino':
        au_casino = random.randrange(-50, 50)
        print(au_casino)
        app.gold = app.gold + int(au_casino)
        print('casino')
        activity = "Earned {} gold from the {}! ({})".format(app.gold, request.form['location'], datetime.datetime.now())
        session['activity'] = activity
        print(activity)

    return redirect('/')


if __name__ == '__main__':
    app.run()
