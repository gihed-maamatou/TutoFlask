def test_auteurs_url(client):
    response = client.get('/auteurs/')
    assert response.status_code == 200


def test_auteurs_content(client):
    response = client.get('/auteurs/')
    assert b'Liste des auteurs' in response.data
    assert b"Nombre d'auteurs" in response.data
    assert b'Nombre de livres' in response.data