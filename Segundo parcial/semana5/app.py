
from flask import Flask, request, url_for, render_template, redirect
from database import db
from flask_migrate import Migrate
from models import Persona
from forms import PersonaForm
app = Flask(__name__)


#Configurar la db
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'test_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#Configurar migracion
migrate = Migrate()
migrate.init_app(app,db)


# Secret key

app.config['SECRET_KEY'] = "amsfnu3r3u73739klndfosdfh43ioh3i9hofnkdlfnlsdkjflks"

#Rutas de flask

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def inicio():
    personas = Persona.query.all()
    return render_template('index.html', personas=personas)

@app.route("/ver/<int:id>")
def verDetalle(id):
    persona = Persona.query.get_or_404(id)
    return render_template('detalle.html', persona=persona)

@app.route("/agregar", methods = ['GET','POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            # Insert a la db
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = personaForm)


@app.route("/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            #Update a la db, no es necesario hacer nada mas.
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma = personaForm)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))

## Correr codigo = flask db init = crear carpetas proyecto
## Empezar migraciones = flask db migrate = crear tabla default
## Hacer migraciones = flask db upgrade = actualizar
## Instalar formas = pip install flask-wtf