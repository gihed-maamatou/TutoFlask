from flask import redirect, render_template, url_for
from . import livres_bp
from .forms import FormLivrePrix
from monApp.app import db
from monApp.models import Livre

@livres_bp.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template('livres_list.html', title="R3.01 Dev Web avec Flask", livres = lesLivres)


@livres_bp.route("/livres/<int:idL>/view/")
def viewLivre(idL):
    unLivre = db.session.get(Livre, idL)
    if unLivre is None:
        return "Livre introuvable", 404

    return render_template(
        "livre_view.html",
        title="Consultation d'un livre",
        selectedLivre=unLivre,
    )


@livres_bp.route("/livres/<int:idL>/update/")
def updateLivre(idL):
    unLivre = db.session.get(Livre, idL)
    if unLivre is None:
        return "Livre introuvable", 404

    return render_template(
        "livre_update.html",
        title="Modifier un livre",
        selectedLivre=unLivre,
        updateForm=FormLivrePrix(idL=unLivre.idL, Prix=unLivre.Prix),
    )


@livres_bp.route("/livre/save/", methods=("POST",))
def saveLivre():
    updateForm = FormLivrePrix()
    idL = updateForm.idL.data
    updatedLivre = db.session.get(Livre, idL) if idL else None

    if updatedLivre is None:
        return "Livre introuvable", 404

    if updateForm.validate_on_submit():
        updatedLivre.Prix = updateForm.Prix.data
        db.session.commit()
        return redirect(url_for("livres.viewLivre", idL=updatedLivre.idL))

    return render_template(
        "livre_update.html",
        title="Modifier un livre",
        selectedLivre=updatedLivre,
        updateForm=updateForm,
    ), 400