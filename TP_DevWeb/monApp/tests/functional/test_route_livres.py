from monApp.app import db
from monApp.models import Livre


def test_livres_url(client):
    response = client.get('/livres/')
    assert response.status_code == 200


def test_livres_content(client):
    response = client.get('/livres/')
    assert b'Liste des livres' in response.data
    assert b'Titre' in response.data
    assert b'Prix' in response.data
    assert b'Premiere de couverture' in response.data
    assert b'Auteur' in response.data


def test_livre_views(client, testapp):
    with testapp.app_context():
        livre = Livre(
            Prix=10,
            Titre="Livre de test",
            Url="https://example.com",
            Img="",
            auteur_id=1,
        )
        db.session.add(livre)
        db.session.commit()
        id_livre = livre.idL

    assert client.get(f"/livres/{id_livre}/view/").status_code == 200
    assert client.get(f"/livres/{id_livre}/update/").status_code == 200
