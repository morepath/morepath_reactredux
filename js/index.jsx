import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import AnimalsContainer from './container';
import { store } from './store';

const targetEl = document.getElementById('root');

ReactDOM.render(
  <Provider store={store}>
      <AnimalsContainer />
  </Provider>,
  targetEl
);
