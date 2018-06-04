from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key='Keep it safe'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # flash("process started")
    #do validation here
    print(len(''))
    print(len('hello'))
    if len(request.form['name']) < 2:
        print("the name is too short")
        flash("Name cannot be empty!")
        # display validation errors
    else:
        # display success message
        print("the name is valid")
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/')




if __name__ == '__main__':
    app.run()
