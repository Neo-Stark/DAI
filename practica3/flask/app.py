# ./flask/app.py

from flask import (Flask, render_template, session, request, redirect, url_for)
import os.path
from pickleshare import *
import logging

app = Flask(__name__)
app.secret_key = '1234'
app.debug=True
db = PickleShareDB('practica3DB')

def renderizar(ruta, template, **context):
    if 'user' in session:
        paginasVisitadas(ruta)
        template = render_template(template, user=session['user'], paginas=session['paginas'], **context)
    elif 'error' in session:
        template = render_template(template, error=session['error'], **context)
    else:
        template = render_template(template, **context)

    if 'error' in session:
        session.pop('error')
    return template

@app.route('/')
def index():
    return renderizar('/', 'index.html')


@app.route('/buscar')
def buscar():
    return renderizar('/buscar', 'busqueda.html')


@app.route('/catalogo')
def catalogo():
    return renderizar('/catalogo', 'catalogo.html')


@app.route('/tiendas')
def tiendas():
    return renderizar('/tiendas', 'tiendas.html')    


@app.route('/pedidos')
def pedidos():
    return renderizar('/pedidos', 'pedidos.html')



@app.route("/login", methods=['POST'])
def login():
    user = request.form['user']
    passwd = request.form['pass']
    session.clear()
    if (db.keys(user) and db[user] == passwd):
        session["user"] = user
        session["auth"] = passwd
        return redirect(url_for('index'))
    else:
        session['error'] = 'usuario o contraseña incorrectos'
        return redirect(url_for('index'))
        


@app.route("/logout")
def logout():
    session.clear()
    return index()

@app.route("/registrar")
def registrar():
    if 'errorRegistro' in session and 'usuario' in session:
        return renderizar('registrar','usuario.html', usuario=session['usuario'], errorRegistro = session['errorRegistro'])
    elif 'usuario' in session:
        session.pop('usuario')
        return renderizar('registrar', 'registrado.html')
    else:
        return renderizar('registrar', 'usuario.html')

@app.route("/registrando", methods=['POST'])
def registrando():
    if 'usuario' in request.form:
        print(request.form, file=sys.stderr)
        usuario = request.form['usuario']
        session['usuario'] = usuario
        pass1 =   request.form['pass']    
        pass2 =   request.form['pass2']
        if pass1 != pass2:
            session['errorRegistro'] = "Las contraseñas no coinciden"
        else:
            if 'errorRegistro' in session: session.pop('errorRegistro')
            db[usuario] = pass1
    return redirect(url_for('registrar'))


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Página no encontrada", 404


def paginasVisitadas(pag):
    if 'paginas' in session and len(session['paginas']) > 2:
        session['paginas'].append(pag)
        session['paginas'].pop(0)
        session['paginas'] = session['paginas']
    elif 'paginas' in session:
        session.get('paginas').append(pag)
        session['paginas'] = session['paginas']
    else:
        session['paginas'] = []
