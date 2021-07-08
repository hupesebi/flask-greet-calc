# Put your app in here.
from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def adding():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def subtracting():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def multiplying():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def dividing():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

operators={
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult,

@app.route('/math/<op>')
def do_math(op):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[op](a,b)
    return str(result)