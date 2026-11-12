from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField
from wtforms.validators import DataRequired

class FormAuteur(FlaskForm):
    idA = HiddenField("idA")
    Nom = StringField("Nom", validators=[DataRequired()])
