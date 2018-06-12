from flask import Flask, session, redirect, request, render_template

app = Flask(__name__)
app.secret_key="shhhh keep this secret"

app.count = 0

@app.route('/')
def index():
    session['count']=app.count
    print(session['count'])
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    app.count = session['count']+1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    app.count = 0
    return redirect('/')




if __name__ == '__main__':
    app.run()
