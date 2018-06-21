from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import connectToMySQL
import re
from time import time
from datetime import datetime, date

EMRX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secret for the email validation"
EMAIL_REGEX = EMRX

mysql = connectToMySQL('emails_db')
print(mysql)
print('all the emails:', mysql.query_db('SELECT * FROM emails;'))


@app.route('/')
def index():
    all_emails = mysql.query_db('SELECT * FROM emails')
    print('Fetched all email addresses:', all_emails)
    type(all_emails)
    list_len = len(all_emails)
    session['list_len'] = list_len

    print(list_len)
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    email = request.form['email']
    print(email)
    all_email_addresses = mysql.query_db('SELECT email_address FROM emails_db.emails')
    email_length = len(all_email_addresses)
    print(email_length)
    for email_length in all_email_addresses:
        print(email_length['email_address'])
        if email_length['email_address'] == email:
            print('a match')
            flash('This email address already exists.')
            return redirect('/')

    if len(request.form['email']) == 0:
        flash('Email cannot be blank')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(('Invalid email address'))
        return redirect('/')
    else:
        session['email'] = request.form['email']
        query = "INSERT INTO emails (email_address, created_at) VALUES (%(email_address)s, NOW());"
        data = {
            'email_address':email,
        }
        mysql.query_db(query, data)
        return redirect('/success')


@app.route('/success')
def success():
    email = session['email']
    flash('The email address you entered (' + email + ') is a VALID email address! Thank you')
    print("+" * 50)
    all_emails = mysql.query_db('SELECT * FROM emails')
    print(all_emails)
    print(email)
    print("+" * 50)
    print(session['list_len'])
    return render_template('success.html', emails = all_emails, list_len = session['list_len'])



if __name__ == '__main__':
    app.run(debug=True)
