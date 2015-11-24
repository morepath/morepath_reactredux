import morepath
from webtest import TestApp as Client
import webui
from .. import fakedb
from ..app import App


def setup_module(module):
    config = morepath.setup()
    config.scan(webui)
    config.commit()


def teardown_function(function):
    fakedb.reset_zoo()


def test_root():
    c = Client(App())

    response = c.get('/')
    assert response.json == {"collection": "http://localhost/animals"}
