from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/dojo')
def dojo():
    return 'Dojo'


@app.route('/say/<name>')  # will return 'Hi' to any name passed to the url
def say(name):
    print(name)
    return 'Hi ' + name


@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    print( word * int(num))
    return word * int(num)


# @app.route('/')
# def hello_world():
#     return 'Hello World'
#

if __name__ == '__main__':
    app.run(debug=True)
