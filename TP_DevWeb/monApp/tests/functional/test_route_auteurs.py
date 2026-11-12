def test_auteurs_url(client):
    response = client.get('/auteurs/')
    assert response.status_code == 200


def test_auteurs_content(client):
    response = client.get('/auteurs/')
    assert b'Liste des auteurs' in response.data
    assert b"Nombre d'auteurs" in response.data
    assert b'Nombre de livres' in response.data


def test_view_auteur(client):
    response = client.get("/auteurs/1/view/")
    assert response.status_code == 200
    assert b"Victor Hugo" in response.data


def test_update_auteur(client):
    response = client.get("/auteurs/1/update/")
    assert response.status_code == 200
    assert b"Modification de l'auteur Victor Hugo" in response.data


def test_create_auteur(client):
    response = client.get("/auteur/")
    assert response.status_code == 200
    assert b"Cr\xc3\xa9ation d'un auteur" in response.data


def test_delete_auteur(client):
    response = client.get("/auteurs/1/delete/")
    assert response.status_code == 200
    assert b"Suppression de l'auteur Victor Hugo" in response.data