from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "this is my secret pass key"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/all_four', methods=['POST'])
def all_four():
    return render_template("ninjas.html")


@app.route('/ninja', methods=['POST'])
def ninja():
    session['color'] = request.form['color']

    print "This is the Session Color: " + session['color']
    ninja_color = session['color']

    return render_template("/"+ninja_color + ".html")


if __name__ == '__main__':
    app.run()
