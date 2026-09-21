from monApp.models import Auteur

def test_auteur_init(): 
    auteur = Auteur("Cricri DAL")
    assert auteur.Nom == "Cricri DAL"

def test_auteur_getters_setters():
    auteur = Auteur("Tof DAL")
    assert auteur.get_nom() == "Tof DAL"
    auteur.set_nom("CDAL")
    assert auteur.get_nom() == "CDAL"

def test_auteur_idA():
    auteur = Auteur("Test ID")
    assert auteur.get_idA() is None
    auteur.set_idA(1)
    assert auteur.get_idA() == 1

def test_toString(): 
    auteur = Auteur("Test Affichage")
    auteur.set_idA(2)
    assert auteur.__repr__() == "<Auteur (2) Test Affichage>"