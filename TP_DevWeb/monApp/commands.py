import click, logging as lg
from flask.cli import with_appcontext
from .app import db



def register_commands(app):
    app.cli.add_command(loaddb)



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