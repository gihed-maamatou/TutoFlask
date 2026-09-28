def test_index(client):         #client est la fixture définie dans conftest.py
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello world' in response.data

def test_index_cricri(client):
    response = client.get('/index/')
    assert response.status_code == 200
    assert b'Bienvenue Cricri' in response.data


def test_about(client):
    response = client.get('/about/')
    assert response.status_code == 200
    assert b'A savoir sur nous : Rien' in response.data

def test_contact(client):
    reponse = client.get('/contact/')
    assert reponse.status_code == 200
    assert b'vous souhaitez nous contacter : Contactez-moi! Non je rigole, pas envie de recevoir des mails'