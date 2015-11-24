import {LOAD_ANIMALS, ADD_ANIMAL, DELETE_ANIMAL} from './actions';

const initialState = {
  animalsId: null,
  animals: [],
};

export default function update(state = initialState, action) {
  if (action.type === LOAD_ANIMALS) {
    return {
      animals: action.animals,
      animalsId: action.animalsId,
    };
  } else if (action.type === ADD_ANIMAL) {
    const newAnimals = state.animals.slice();
    newAnimals.push({
      '@id': action.animalId,
      name: action.name,
      species: action.species,
    });
    return Object.assign({}, state, {
      animals: newAnimals,
    });
  } else if (action.type === DELETE_ANIMAL) {
    return {
      animals: action.animals,
      animalsId: state.animalsId,
    };
  }
  return state;
}
