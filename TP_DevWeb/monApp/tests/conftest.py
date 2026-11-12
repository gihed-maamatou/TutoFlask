import pytest
from monApp import create_app
from monApp.app import db
from monApp.models import Auteur

@pytest.fixture
def testapp():
    app = create_app("config.TestingConfig")
    with app.app_context():
        db.create_all()
        db.session.add(Auteur(Nom="Victor Hugo"))
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()

@pytest.fixture
def runner(testapp):
    return testapp.test_cli_runner()