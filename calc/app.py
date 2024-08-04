# calc/app.py
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtraction():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def division():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = div(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
