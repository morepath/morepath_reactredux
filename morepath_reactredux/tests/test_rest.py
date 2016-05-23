import morepath
import morepath_reactredux
from morepath_reactredux import App, fakedb

import json
from webtest import TestApp as Client


def setup_module(module):
    morepath.scan(morepath_reactredux)
    morepath.commit(App)


def teardown_function(function):
    fakedb.reset_zoo()


def test_root():
    c = Client(App())

    response = c.get('/')
    assert response.json == {"collection": "http://localhost/animals"}


def test_zoo():
    c = Client(App())
    response = c.get('/animals')
    zoo = {"animals": [
        {"@id": "http://localhost/animals/0",
         "name": "Bob", "species": "snake"},
        {"@id": "http://localhost/animals/1",
         "name": "Fred", "species": "snake"},
        {"@id": "http://localhost/animals/2",
         "name": "Anna", "species": "elephant"},
        {"@id": "http://localhost/animals/3",
         "name": "Kate", "species": "tiger"}
    ]}
    assert response.json == zoo


def test_animal():
    c = Client(App())
    response = c.get('/animals/0')
    assert response.json == {"@id": "http://localhost/animals/0",
                             "name": "Bob", "species": "snake"}


def test_add_animal():
    c = Client(App())

    new_animal_json = json.dumps({"name": "Lupus", "species": "wolf"})
    response = c.post('/animals', new_animal_json)
    new_animal_response = {"@id": "http://localhost/animals/4",
                           "name": "Lupus", "species": "wolf"}
    assert response.json == new_animal_response


def test_delete_animal():
    c = Client(App())

    response = c.delete('/animals/2')
    zoo = {"animals": [
        {"@id": "http://localhost/animals/0",
         "name": "Bob", "species": "snake"},
        {"@id": "http://localhost/animals/1",
         "name": "Fred", "species": "snake"},
        {"@id": "http://localhost/animals/3",
         "name": "Kate", "species": "tiger"}
    ]}
    assert response.json == zoo


def test_change_animal():
    c = Client(App())

    changed_animal_json = json.dumps(
        {"name": "Changed Fred", "species": "fish"}
    )
    response = c.put('/animals/1', changed_animal_json)
    changed_animal_response = {"@id": "http://localhost/animals/1",
                               "name": "Changed Fred", "species": "fish"}
    assert response.json == changed_animal_response
