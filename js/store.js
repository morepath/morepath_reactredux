import thunkMiddleware from 'redux-thunk';
import createLogger from 'redux-logger';
import { createStore, applyMiddleware } from 'redux';
import update from './reducers';
import { loadAnimals } from './actions';

const loggerMiddleware = createLogger();

const createStoreWithMiddleware = applyMiddleware(
  thunkMiddleware,
  loggerMiddleware)(createStore);

export const store = createStoreWithMiddleware(update);

store.dispatch(loadAnimals('/api/animals'));

