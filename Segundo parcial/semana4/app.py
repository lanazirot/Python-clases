import logging
from flask import Flask, jsonify, render_template, request, session, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
app = Flask(__name__)

logging.basicConfig(filename='error.log', level=logging.DEBUG)

# Sesiones
app.secret_key = '(*&^%$%^&UIKMNBVCDSW#$%^&*(Onhasdhbnewor98yeuj'

@app.before_request()
def verificarSesion():
    if not session:
        return redirect(url_for('login'))

@app.route("/")
def holaMundo():
    if 'username' in session:
        app.logger.debug("Entrando a la pagina principal desde IP: SuperIP")
        return render_template('/index/index.html', currentSesion=session)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('clientes'))
    return render_template('login.html')
        
@app.route('/logout')
def logout():
    if session:
        session.pop('username')
    return redirect(url_for('login'))


@app.route("/clientes")
def clientes():
    data = [
        {
            "Nombre": "Alan"
        },
        {
            "Nombre": "Jesus"
        },
        {
            "Nombre": "Jesus"
        }
    ]
    return render_template("/clientes/listaClientes.html", clientes=data)


@app.route("/clientes/<int:id>")
def cliente(id):
    if id == 20:
        return jsonify({'message': 'Error, es 20', 'data': None})
    else:
        return jsonify({'message': 'Gracias a Diosito no es 20', 'data': 20})


@app.route('/juego', methods=['POST'])
def insertarJuego():
    token = request.headers.get('token')
    app.logger.debug(f'TOKEN = {token}')
    data = request.get_json()
    nombre = data['nombre']
    precio = data['precio']
    calificacion = data['calificacion']

    return f'Juego es {nombre} de  precio {precio} con calificacion {calificacion}'


@app.route('/juego/<int:id>', methods=['GET'])
def mostrarJuego(id):
    data = {'id': id, 'nombre': 'Super Mario'}
    return jsonify(data)


@app.route("/edad/<int:edad>", methods=['POST', 'GET'])
def edad(edad):
    return f'La edad es {edad}'


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html', error=error), 404
