def test_index(client):         #client est la fixture définie dans conftest.py
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello world' in response.data