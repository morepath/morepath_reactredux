export const LOAD_ANIMALS = 'LOAD_ANIMALS';
export function loadAnimals(animalsId) {
  return (dispatch) => {
    return fetch(animalsId)
      .then(response => response.json())
      .then(json => {
        dispatch({
          type: LOAD_ANIMALS,
          animalsId: animalsId,
          animals: json.animals,
        });
      });
  };
}

export const ADD_ANIMAL = 'ADD_ANIMAL';
export function addAnimal(name, species) {
  return (dispatch, getState) => {
    const animalsId = getState().animalsId;
    return fetch(animalsId, {
      method: 'POST',
      body: JSON.stringify({
        name,
        species,
      }),
    })
      .then(response => response.json())
      .then(json => {
        dispatch({
          type: ADD_ANIMAL,
          animalId: json['@id'],
          name: json.name,
          species: json.species,
        });
      });
  };
}

export const DELETE_ANIMAL = 'DELETE_ANIMAL';
export function deleteAnimal(animalId) {
  return (dispatch) => {
    return fetch(animalId, {
      method: 'DELETE',
    })
      .then(response => response.json())
      .then(json => {
        dispatch({
          type: DELETE_ANIMAL,
          animals: json.animals,
        });
      });
  };
}
