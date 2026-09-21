from monApp.models import Livre


def test_livre_init():
    livre = Livre(12.5, "Le titre", "example.com", "couverture.jpg")
    assert livre.Prix == 12.5
    assert livre.Titre == "Le titre"
    assert livre.Url == "example.com"
    assert livre.Img == "couverture.jpg"


def test_livre_getters_setters():
    livre = Livre(12.5, "Le titre", "example.com", "couverture.jpg")
    livre.set_prix(9.99)
    livre.set_titre("Nouveau titre")
    livre.set_url("example.org")
    livre.set_img("nouvelle-couverture.jpg")
    assert livre.get_prix() == 9.99
    assert livre.get_titre() == "Nouveau titre"
    assert livre.get_url() == "example.org"
    assert livre.get_img() == "nouvelle-couverture.jpg"


def test_livre_idL():
    livre = Livre(12.5, "Le titre", "example.com", "couverture.jpg")
    assert livre.get_idL() is None
    livre.set_idL(3)
    assert livre.get_idL() == 3


def test_livre_to_string():
    livre = Livre(12.5, "Le titre", "example.com", "couverture.jpg")
    livre.set_idL(3)
    assert repr(livre) == "<Livre (3) Le titre>"