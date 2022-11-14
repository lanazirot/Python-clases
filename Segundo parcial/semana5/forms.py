from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    # Campos necesarios
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    
    # Boton para enviar datos.
    enviar = SubmitField("Enviar datos")
    
    