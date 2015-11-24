from .app import App
from .fakedb import Zoo, Animal, zoo
from .model import Root


@App.path(path='/', model=Root)
def get_root():
    return Root()


@App.path(path='/animals', model=Zoo)
def get_zoo():
    return zoo


@App.path(path='/animals/{id}', model=Animal)
def get_animal(id=0):
    return zoo.get(id)
