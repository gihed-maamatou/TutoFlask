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
