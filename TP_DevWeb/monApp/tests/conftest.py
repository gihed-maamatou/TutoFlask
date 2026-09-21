import pytest
from monApp import app

@pytest.fixture
def testapp():
    return app

@pytest.fixture
def client(testapp):
    return testapp.test_client()

@pytest.fixture
def runner(testapp):
    return testapp.test_cli_runner()