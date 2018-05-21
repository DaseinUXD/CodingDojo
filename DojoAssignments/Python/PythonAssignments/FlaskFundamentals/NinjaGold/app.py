from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "this is the secret key"
app.gold = 0
@app.route('/', methods=['POST', 'GET'])
def index():
    session.gold = app.gold
    # print(type(session.gold))
    return render_template(' index.html')

@app.route('/process_money', methods=['POST', 'GET'])
def process_money():
    if request.form['location'] == 'farm':
        print('this is the farm input')
        session.farmGold = random.randrange(10,21)
        print(request.form['location'])
        app.gold = app.gold + session.farmGold
        # return redirect('/')

    if request.form['location'] == 'cave':
        print('this is the cave input')
        session.caveGold = random.randrange(5,11)
        print(request.form['location'])
        app.gold = app.gold + session.caveGold
        # return redirect('/')

    if request.form['location'] == 'house':
        print('this is the house input')
        session.houseGold = random.randrange(2,6)
        print(request.form['location'])
        app.gold = app.gold + session.houseGold
        # return redirect('/')

    if request.form['location'] == 'casino':
        print('this is the cave input')
        session.casinoGold = random.randrange(-50,51)
        print(request.form['location'])
        app.gold = app.gold + session.casinoGold
        # return redirect('/')
    return redirect('/')


if __name__ == '__main__':
    app.run()
