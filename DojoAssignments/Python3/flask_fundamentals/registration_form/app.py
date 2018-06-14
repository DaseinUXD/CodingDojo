from flask import Flask, redirect, request, render_template, session, flash
import datetime
import re

P = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'this is my secret, what is yours?'
EMAIL_REGEX = P
PASS_CAP = re.compile(r'[A-Z]{1}')
PASS_NUM = re.compile(r'\d')

now = datetime.date.today()


@app.route('/')
def index():
    print(type(now))
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    # First Name
    if len(request.form['first_name']) == 0:
        flash('First name cannot be blank')
    elif request.form['first_name'].isalpha() == False:
        flash('First name may contain only letters, no numbers')
    # Last Name
    if len(request.form['last_name']) == 0:
        flash('Last name cannot be blank')
    elif request.form['last_name'].isalpha() == False:
        flash('Last name may contain only letters, no numbers')
    # Email
    if len(request.form['email']) == 0:
        flash('Email cannot be blank')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address')
    if request.form['birth_date'] >= str(now):
        flash('Birthday must be in the future')
    # Password
    if len(request.form['password']) == 0:
        flash('Password cannot be blank')
    elif len(request.form['password']) < 8:
        flash('Password should be more than 8 characters')
    elif not PASS_CAP.match(request.form['password']):
        flash('Password should have at least one capital letter')
    elif not PASS_NUM.match(request.form['password']):
        flash('Password should have at least one numeric value')
    # Confirmation
    if len(request.form['confirm']) == 0:
        flash('Confirm password cannot be blank')
    if request.form['password'] != request.form['confirm']:
        flash('The password confirmation does not match your password')
    else:
        flash('Thanks for submitting your information')

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['birth_date'] = request.form['birth_date']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']
    return redirect('/')


if __name__ == '__main__':
    app.run()
#
