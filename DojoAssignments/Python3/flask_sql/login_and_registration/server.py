from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "one more secret to keep track of"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}')

mysql = connectToMySQL('login_registration')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    # Validation and Error Checking
    first_name = request.form['first_name']  # Letters only, at least 2 characters and that it was submitted
    last_name = request.form['last_name']  # Letters only, at least 2 characters and that it was submitted
    email = request.form[
        'email']  # Valid email format, does not already exist in the database, and that it was submitted
    password = request.form['password']  # At least 8 characters, and that it was submitted
    password_confirm = request.form['password_confirm']  # matches password

    # Set session variables for name and email to fill in after error submission
    session['first_name'] = first_name
    session['last_name'] = last_name
    session['email'] = email

    # Gather email addresses from database for verification.
    # collect all email addresses in the database
    all_emails = mysql.query_db('SELECT email FROM registered_users')  # This is returned as a dictionary
    # get the total number of emails in the database; which will be used to build a range for
    # iterating through the emails and compare with the one currently submitted
    num_of_emails = len(all_emails)
    for i in range(num_of_emails):
        if all_emails[i][
            'email'] == email:  # iterate through each listing in the dictionary and collect all the values,
            # which are the email addresses
            # step-wise compare each of these with the email submitted
            flash('A user is already registered with this email address.', 'email')
            return redirect('/')

    # Validate first and last name
    if len(first_name) < 2:
        flash('First name must be at least two characters long', 'first_name')
    elif not first_name.isalpha():
        flash('First name may only contain letters, no numbers', 'first_name')
        return redirect('/')

    if len(last_name) < 2:
        flash('Last name must be at least two characters long', 'last_name')
    elif not last_name.isalpha():
        flash('Last name may only contain letters, no numbers', 'first_name')
        return redirect('/')

    #  Validate email address
    if not EMAIL_REGEX.match(email):
        flash('Please enter a valid email address', 'email')
        # return redirect('/')

    # Validate and match password entries
    if not PASSWORD_REGEX.match(password):
        flash('Please choose a valid password', 'password')
    elif password_confirm != password:
        flash('Your passwords did not match', 'password_confirm')
        return redirect('/')
    else:
        # query = "INSERT INTO registered_users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW()"
        # data = {
        #     'first_name':first_name,
        #     'last_name':last_name,
        #     'email':email,
        #     'password':password,
        # }
        # mysql.query_db(query, data)
        return redirect('/success')


@app.route('/login', methods=['POST'])
def login():
    login_email = request.form[
        'login_email']  # Valid email format, does not already exist in the database, and that it was submitted
    login_password = request.form['login_password']  # At least 8 characters, and that it was submitted

    # Gather email addresses from database for verification.
    # collect all email addresses in the database

    all_emails = mysql.query_db('SELECT email FROM registered_users')  # This is returned as a dictionary

    num_of_emails = len(all_emails)
    # get the total number of emails in the database; which will be used to build a range for
    # iterating through the emails and compare with the one currently submitted
    for i in range(num_of_emails):
        if not all_emails[i]['email'] == login_email:
            # iterate through each listing in the dictionary and collect all the values,
            # which are the email addresses
            # step-wise compare each of these with the email submitted
            flash('There is no registered user with this email address.', 'email')
            return redirect('/')

    return redirect('/success')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
