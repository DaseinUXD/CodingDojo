from flask import Flask, session, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key='secret'

# landing page
@app.route('/')
def index():
    return render_template('index.html')



# results page
@app.route('/result')
def result():
    return render_template('result.html')

#submission route
@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['comment'] = request.form['comment']
    session['location'] = request.form['location']
    session['language'] = request.form['language']

    return redirect('/result')





if __name__ == '__main__':
    app.run()
