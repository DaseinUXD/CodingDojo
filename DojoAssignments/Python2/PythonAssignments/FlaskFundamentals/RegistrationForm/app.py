from flask import Flask, session, flash, redirect, request, render_template
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

f_name_regex = re.compile(r'^([^0-9]*)$')
l_name_regex = re.compile(r'^([^0-9]*)$')

app = Flask(__name__)

app.secret_key="the secret is mine"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if len(request.form['first_name']) < 1:
        print('no blank first')
        flash('First Name cannot be blank')
        return render_template('index.html')

    elif not f_name_regex.match(request.form['first_name']):
        flash('First Name may not contain numbers')
        return render_template('index.html')


    if len(request.form['last_name']) < 1:
        print('no blank last')
        flash('Please enter a last name')
        return render_template('index.html')

    elif not f_name_regex.match(request.form['first_name']):
        flash('Last Name may not contain numbers')
        return render_template('index.html')

    if len(request.form['email']) < 1:
        print('no blank email')
        flash('Please enter an email address')
        return render_template('index.html')

    if len(request.form['reg_pwd']) < 8:
        print('no blank reg pwd')
        flash('Passwords must be at least eight (8) characters long')
        return render_template('index.html')

    if len(request.form['conf_pwd']) < 1:
        print('no blank conf pwd')
        flash('Your confirmation password is blank')
        return render_template('index.html')

    regPwd = request.form['reg_pwd']
    confPwd = request.form['conf_pwd']

    if regPwd != confPwd:
        flash('Your passwords do not match')
        return render_template('index.html')

    return render_template('success.html')


if __name__ == '__main__':
    app.run()
