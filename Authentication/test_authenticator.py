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
    app.config.update({"testing": True})

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

class test_class():
    '''Class container for the unit testing of matrix_mult.py'''
    def test_add_user(self,client):
        '''Test adding a user'''
        log.info("Adding user 34")
        response = client.put(BASE + "userlist/34",{"email" : "janesmith@bu.edu", "name" : "Smith, Jane"})
        assert response == 201


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    mytest = test_class()
    mytest.test_add_user(client)
