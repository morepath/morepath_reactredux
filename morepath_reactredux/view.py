from .fakedb import Zoo, Animal, zoo
from .app import App
from .model import Root


@App.json(model=Root)
def root_get(self, request):
    return {
        'collection': request.link(zoo)
    }


@App.json(model=Zoo)
def zoo_get(self, request):
    return {
        'animals': [request.view(animal) for animal in self.get_all()]
    }


@App.json(model=Zoo, request_method='POST')
def zoo_post(self, request):
    animal_json = request.json
    animal = Animal(animal_json['name'], animal_json['species'])
    self.add(animal)

    @request.after
    def after(response):
        response.status = 201

    return request.view(animal)


@App.json(model=Animal)
def animal_get(self, request):
    return {
        '@id': request.link(self),
        'name': self.name,
        'species': self.species
    }


@App.json(model=Animal, request_method='PUT')
def animal_put(self, request):
    animal_json = request.json
    self.name = animal_json['name']
    self.species = animal_json['species']
    return request.view(self)


@App.json(model=Animal, request_method='DELETE')
def animal_delete(self, request):
    zoo.remove(self.id)
    return request.view(zoo)
