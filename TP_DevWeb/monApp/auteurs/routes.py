from flask import render_template
from . import auteurs_bp 
from monApp.models import Auteur
@auteurs_bp.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()  
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)