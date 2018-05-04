from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods = ['POST'])
def process():
    # print 'got post'
    name = request.form['name']
    print name
    # name = request.form['name']

    return redirect('/')

if __name__ == '__main__':
    app.run()
