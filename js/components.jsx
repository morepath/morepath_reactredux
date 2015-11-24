import React from 'react';

function Animal({animal, deleteAnimal}) {
  const handleClick = () => {
    deleteAnimal(animal['@id']);
  };

  return (
    <div>
        <p>The animal {animal.name} is of species {animal.species}
            <button onClick={handleClick}>Delete</button> </p>
    </div>
  );
}

export class Animals extends React.Component {
  render() {
    const {animals, addAnimal, deleteAnimal } = this.props;
    const items = animals.map(animal => {
      return (
        <li key={animal['@id']}>
            <Animal animal={animal} deleteAnimal={deleteAnimal} />
        </li>
      );
    });

    const handleClick = () => {
      addAnimal(this.refs.name.value, this.refs.species.value);
    };

    return (
      <div>
          <ul>
              {items}
          </ul>
          <p>Amount: {animals.length}</p>
          <div>
              <input type="text" ref="name" />
              <input type="text" ref="species" />
              <button onClick={handleClick}>Add</button>
          </div>
      </div>
    );
  }
}

