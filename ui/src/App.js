import logo from './logo.svg';
import './App.css';
import {Nav} from '../components';
import {User} from '../templates';
import {BrowserRouter as Router, Route, Switch } from 'react-router';

function App() {
  return <>
    {/* <User>Hello React</User> */}
    <Nav></Nav>
    <Router>
      <Switch>
        <Route path="/user" component ={User}/>
      </Switch>
    </Router>
  </>
}

export default App;
