from flask import render_template
from . import auteurs_bp 
from monApp.models import Livre
@auteurs_bp.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template('livres_list.html', title="R3.01 Dev Web avec Flask", livres = lesLivres)