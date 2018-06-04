from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'this is the secret key'


# landing page
@app.route('/')
def index():
    return render_template('index.html')


# results page
@app.route('/result', methods=['GET', 'POST'])
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
    if len(request.form['name']) > 1 and len(request.form['comment']) > 1 and len(request.form['comment']) < 121:

        return redirect('/result')
    else:
        if len(request.form['name']) < 1:
            flash("Name cannot be blank")
            print('name not empty')
            return redirect('/')
        elif len(request.form['comment']) < 1:
            flash("Comments section cannot be blank")
            return redirect('/')
        elif len(request.form['comment']) > 120:
            flash("Comments must be limited to 120 characters or fewer")
            return redirect('/')





if __name__ == '__main__':
    app.run()
