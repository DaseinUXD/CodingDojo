from flask import Flask,request, redirect, render_template, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key="shhh, be very very quiet, i'm hunting wabbit"

mysql = connectToMySQL('friendsdb')
print(mysql)
print('all the users', mysql.query_db("SELECT * FROM friends;"))

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    print('Fetched all friends', all_friends)
    print(all_friends)
    type(all_friends)
    list = len(all_friends)
    print(list)
    return render_template('index.html', friends = all_friends, list=list)

@app.route('/create_friend', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    # query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW();"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation'],
    }

    mysql.query_db(query, data)

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

