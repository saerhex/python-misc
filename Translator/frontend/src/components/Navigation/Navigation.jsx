import React from "react"
import WordsInput from "../Input/WordsInput"
import Translation from "../Translation/Translation"
import Home from "../App/Home"
import {
  BrowserRouter as Router,
  Link,
  Switch,
  Route
} from 'react-router-dom'


const NavBar = () => {
  return (
    <Router>
      <nav>
        <div className="nav-wrapper teal">
          <div className="brand-logo center">
            <ul id="nav-mobile" className="right hide-on-med-and-down">
              <li><Link to="/translate">Translate</Link></li>
              <li><Link to="/add-words">Add words</Link></li>
              <li><Link to="/">Home</Link></li>
            </ul>
          </div>
        </div>
      </nav>
      <Switch>
        <div className="container">
          <div className="center" style={{paddingTop: 160}}>
            <Route path="/add-words" component={WordsInput}/>
            <Route path="/translate" component={Translation}/>
            <Route path="/" exact component={Home}/></div>
        </div>
      </Switch>
    </Router>
  )
}

export default NavBar