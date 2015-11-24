import { bindActionCreators} from 'redux';
import { connect } from 'react-redux';
import { addAnimal, deleteAnimal } from './actions';
import { Animals } from './components';

function mapStateToProps(state) {
  return {
    animals: state.animals,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    addAnimal: bindActionCreators(addAnimal, dispatch),
    deleteAnimal: bindActionCreators(deleteAnimal, dispatch),
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Animals);
