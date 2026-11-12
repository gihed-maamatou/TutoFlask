import click
import logging as lg
from hashlib import sha256
from flask.cli import with_appcontext
from .app import db



def register_commands(app):
    app.cli.add_command(loaddb)
    app.cli.add_command(syncdb)
    app.cli.add_command(newuser)
    app.cli.add_command(newpasswrd)



@click.command("loaddb")
@click.argument("filename")
@with_appcontext
def loaddb(filename):
    """Creates the tables and populates them with data."""
    db.drop_all()
    db.create_all()

    import yaml
    with open(filename, "r") as file:
        lesLivres = yaml.safe_load(file)

    from .models import Auteur, Livre

    # première passe : création de tous les auteurs
    lesAuteurs = {}
    for livre in lesLivres:
        auteur = livre["author"]
        if auteur not in lesAuteurs :
            objet = Auteur(Nom=auteur)
            db.session.add(objet)
            lesAuteurs[auteur] = objet
    db.session.commit()

    # deuxième passe : création de tous les livres
    for livre in lesLivres:
        auteur = lesAuteurs[livre["author"]]
        objet = Livre(Prix=livre["price"],
                      Titre=livre["title"],
                      Url=livre["url"],
                      Img=livre["img"],
                      auteur_id=auteur.idA)
        db.session.add(objet)
    db.session.commit()
    lg.warning("Database initialized!")


def hash_password(password):
    return sha256(password.encode()).hexdigest()


@click.command("syncdb")
@with_appcontext
def syncdb():
    """Creates all missing tables."""
    db.create_all()
    lg.warning("Database synchronized!")


@click.command("newuser")
@click.argument("login")
@click.argument("pwd")
@with_appcontext
def newuser(login, pwd):
    """Adds a new user."""
    from .models import User

    if db.session.get(User, login) is not None:
        raise click.ClickException(f"User {login} already exists.")

    db.session.add(User(Login=login, Password=hash_password(pwd)))
    db.session.commit()
    lg.warning("User " + login + " created!")


@click.command("newpasswrd")
@click.argument("login")
@click.argument("pwd")
@with_appcontext
def newpasswrd(login, pwd):
    """Changes a user's password."""
    from .models import User

    user = db.session.get(User, login)
    if user is None:
        raise click.ClickException(f"User {login} does not exist.")

    user.Password = hash_password(pwd)
    db.session.commit()
    lg.warning("Password for user " + login + " changed!")