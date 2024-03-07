'''Unit tests for the authenticator module'''
import logging
import tracemalloc
import pytest
import subprocess
import authenticator as auth
import requests

BASE = "http://127.0.0.1:5000/"

tracemalloc.start()

log = logging.getLogger('Test.authenticator')

@pytest.fixture()
def app():
    app = auth.create_app('')
    app.config['TESTING'] = True

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_invalid_user(client):
    log.info("Testing an invalid get")
    response = client.get("/userlist/-97")
    assert response.status_code == 404

def test_add_user(client):
    '''Test adding a user'''
    log.info("Adding user 34")
    response = client.put("/userlist/34",data={"email" : "janesmith@bu.edu", "name" : "Smith, Jane"})
    assert response.status_code == 201


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    pytest.main()
