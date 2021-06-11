import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { Login, Signup, UserDetail, UserEdit, UserList } from 'user/components'
//import { TodoInput, TodoList } from 'todos/components'
import { Home, User, Counter, Article, Item } from 'templates'
import { Nav } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'
import { todoReducer } from 'store'
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
const rootReducer = combineReducers({todoReducer})


const App = () => {
  return (<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>
        <Nav/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'./home'}/>

        <Route exact path='/counter' component={Counter}/>

        <Route exact path='/user' component={User}/>
        <Route exact path='/login-form' component={Login}/>
        <Route exact path='/signup-form' component={Signup}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-list' component={UserList}/>
        <Route exact path='/user-edit' component={UserEdit}/>

        <Route exact path='/article' component={Article}/>

        <Route exact path='/item' component={Item}/>
        
      </Provider>
   </Router>  
  </div>)
 
}

export default App