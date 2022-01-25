from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius>')
def greet(celsius=""):
    return f"{celsius} Celsius is {float(celsius) * 9.0 / 5 + 32} Fahrenheit"


if __name__ == '__main__':
    app.run()
