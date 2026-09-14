def test_index(client):         #client est la fixture définie dans conftest.py
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello world' in response.data


def test_about(client):
    response = client.get('/about/')
    assert response.status_code == 200
    assert b'A propos de ce projet!' in response.data

def test_contact(client):
    reponse = client.get('/contact/')
    assert reponse.status_code == 200
    assert b'Contactez-moi! Non je rigole, pas envie de recevoir des mails'