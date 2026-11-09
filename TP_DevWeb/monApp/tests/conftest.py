import pytest
from monApp import create_app

@pytest.fixture
def testapp():
    app = create_app()
    return app

@pytest.fixture
def client(testapp):
    return testapp.test_client()

@pytest.fixture
def runner(testapp):
    return testapp.test_cli_runner()