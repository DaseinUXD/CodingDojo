from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    for i in request.form:
        print(request.form[i])
    s = request.form['strawberry']
    r = request.form['raspberry']
    a = request.form['apple']
    total = (int(s) + int(r) + int(a))
    now = datetime.datetime.now()
    print(now)

    return render_template('checkout.html', total=total, now=now)


if __name__ == '__main__':
    app.run()
