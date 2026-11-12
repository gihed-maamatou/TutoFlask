from flask_wtf import FlaskForm
from wtforms import DecimalField, HiddenField, StringField
from wtforms.validators import DataRequired

class FormLivre(FlaskForm):
    idL = HiddenField("idL")
    Titre = StringField("Titre", validators=[DataRequired()])
    Prix = DecimalField("Prix", validators=[DataRequired()])
    Url = StringField("Url Amazon")
    Img = StringField("Premiere de couverture")
    auteur = StringField("Auteur associé", validators=[DataRequired()])


class FormLivrePrix(FlaskForm):
    idL = HiddenField("idL")
    Prix = DecimalField("Prix", validators=[DataRequired()])