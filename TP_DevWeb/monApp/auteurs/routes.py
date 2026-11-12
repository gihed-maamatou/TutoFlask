from flask import redirect, render_template, url_for
from . import auteurs_bp
from .forms import FormAuteur
from monApp.models import Auteur
from monApp.app import db


@auteurs_bp.route("/auteurs/")
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template("auteurs_list.html", title="Liste des auteurs", auteurs=lesAuteurs)


@auteurs_bp.route("/auteurs/<int:idA>/update/")
def updateAuteur(idA):
    unAuteur = db.session.get(Auteur, idA)

    if unAuteur is None:
        return "Auteur introuvable", 404

    unForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)

    return render_template(
        "auteur_update.html",
        selectedAuteur=unAuteur,
        updateForm=unForm
    )


@auteurs_bp.route("/auteur/save/", methods=("POST",))
def saveAuteur():
    unForm = FormAuteur()
    idA = unForm.idA.data
    updatedAuteur = db.session.get(Auteur, idA) if idA else None

    if updatedAuteur is None:
        return "Auteur introuvable", 404

    if unForm.validate_on_submit():
        updatedAuteur.Nom = unForm.Nom.data
        db.session.commit()
        return redirect(url_for("auteurs.viewAuteur", idA=updatedAuteur.idA))

    return render_template(
        "auteur_update.html",
        selectedAuteur=updatedAuteur,
        updateForm=unForm,
    ), 400


@auteurs_bp.route("/auteurs/<int:idA>/view/")
def viewAuteur(idA):
    unAuteur = db.session.get(Auteur, idA)
    if unAuteur is None:
        return "Auteur introuvable", 404

    viewForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)
    return render_template(
        "auteur_view.html",
        title="Consultation d'un auteur",
        selectedAuteur=unAuteur,
        viewForm=viewForm,
    )


@auteurs_bp.route("/auteur/")
def createAuteur():
    return render_template(
        "auteur_create.html",
        title="Créer un auteur",
        createForm=FormAuteur(),
    )


@auteurs_bp.route("/auteur/insert/", methods=("POST",))
def insertAuteur():
    createForm = FormAuteur()
    if createForm.validate_on_submit():
        insertedAuteur = Auteur(Nom=createForm.Nom.data)
        db.session.add(insertedAuteur)
        db.session.commit()
        return redirect(url_for("auteurs.viewAuteur", idA=insertedAuteur.idA))

    return render_template(
        "auteur_create.html",
        title="Créer un auteur",
        createForm=createForm,
    ), 400


@auteurs_bp.route("/auteurs/<int:idA>/delete/")
def deleteAuteur(idA):
    unAuteur = db.session.get(Auteur, idA)
    if unAuteur is None:
        return "Auteur introuvable", 404

    return render_template(
        "auteur_delete.html",
        title="Supprimer un auteur",
        selectedAuteur=unAuteur,
        deleteForm=FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom),
    )


@auteurs_bp.route("/auteur/erase/", methods=("POST",))
def eraseAuteur():
    deleteForm = FormAuteur()
    idA = deleteForm.idA.data
    deletedAuteur = db.session.get(Auteur, idA) if idA else None

    if deletedAuteur is None:
        return "Auteur introuvable", 404

    if deleteForm.validate_on_submit():
        db.session.delete(deletedAuteur)
        db.session.commit()
        return redirect(url_for("auteurs.getAuteurs"))

    return render_template(
        "auteur_delete.html",
        title="Supprimer un auteur",
        selectedAuteur=deletedAuteur,
        deleteForm=deleteForm,
    ), 400