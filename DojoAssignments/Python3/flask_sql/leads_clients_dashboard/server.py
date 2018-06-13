from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "black hole sun wont you come"

mysql = connectToMySQL('lead_gen_business')
print(mysql)
print('all the users', mysql.query_db("SELECT concat(clients.first_name, ' ', clients.last_name) as full_name FROM clients"))


@app.route('/')
def index():
    all_info = mysql.query_db(
        "SELECT concat(clients.first_name, ' ', clients.last_name) as full_name, count(*) as total_leads FROM clients JOIN sites on clients.client_id = sites.client_id JOIN leads on sites.site_id = leads.site_id GROUP BY clients.client_id")
    print(all_info)
    list = len(all_info)
    print(list)

    return render_template('index.html', info=all_info, list=list)


if __name__ == '__main__':
    app.run(debug=True)

'''
Hint: Here is an example of a query that selects data between a date range

SELECT Date,TotalAllowance FROM Calculation WHERE EmployeeId=1 AND Date >= '2011/02/25' AND Date < '2011/02/28'copy
         
'''