from flask import Flask, session, request, redirect, render_template


app = Flask(__name__)

app.secret_key="its a secret"

app.count = 0

@app.route('/')
def index():
    # app.count = app.count + 3
    # session['count'] = app.count
    session['count'] = app.count
    print (session['count'])
    return render_template ('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    app.count = session['count'] + 2

    print (session['count'])
    return redirect('/')

@app.route('/decrement', methods=['POST'])
def decrement():
    app.count=0
    #
    # app.count = session.pop( 'count')
    print(session['count'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
