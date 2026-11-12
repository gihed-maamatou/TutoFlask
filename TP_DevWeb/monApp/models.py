from .app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    Login = db.Column(db.String(50), primary_key=True)
    Password = db.Column(db.String(64), nullable=False)

    def get_id(self):
        return self.Login


class Auteur(db.Model):
    idA = db.Column( db.Integer, primary_key=True )
    Nom = db.Column( db.String(100) )

    def __init__(self, Nom): 
        self.Nom = Nom

    def get_nom(self):
        return self.Nom

    def set_nom(self, Nom):
        self.Nom = Nom

    def get_idA(self):
        return self.idA

    def set_idA(self, idA):
        self.idA = idA

    def __repr__(self):
        return "<Auteur (%d) %s>" % (self.idA , self.Nom)


class Livre(db.Model):
    idL = db.Column(db.Integer, primary_key=True)
    Prix = db.Column(db.Float)
    Titre = db.Column(db.String(255))
    Url = db.Column(db.String(255))
    Img = db.Column(db.String(255))
    auteur_id = db.Column (db.Integer , db.ForeignKey ("auteur.idA") )
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )

    def __init__(self, Prix, Titre, Url, Img, auteur_id=None):
        self.Prix = Prix
        self.Titre = Titre
        self.Url = Url
        self.Img = Img
        self.auteur_id = auteur_id

    def get_prix(self):
        return self.Prix

    def set_prix(self, Prix):
        self.Prix = Prix

    def get_titre(self):
        return self.Titre

    def set_titre(self, Titre):
        self.Titre = Titre

    def get_url(self):
        return self.Url

    def set_url(self, Url):
        self.Url = Url

    def get_img(self):
        return self.Img

    def set_img(self, Img):
        self.Img = Img

    def get_idL(self):
        return self.idL

    def set_idL(self, idL):
        self.idL = idL

    def __repr__(self):
        return "<Livre (%d) %s>" % (self.idL, self.Titre)