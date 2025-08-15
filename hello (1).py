# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
@app.route('/contextorequisicao')
def con():
    req = request.headers.get('User-Agent')
    return f'<p>Your browser is {req}</p>'

@app.route("/codigostatusdiferente")
def codigostatusdiferente():
    codigo = request.args["codigo"]
    return f'<p>{codigo}</p>'

@app.route('/objetoresposta')
def objeto_resposta():
    response = make_response('<h1>This document carries a cookie!</h1>' )
    response.set_cookie('answer', '42')
    return response

@app.route('/abortar')
def abortar():
    abort(404)

@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')