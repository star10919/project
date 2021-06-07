import React from 'react'
import { Route } from "react-router-dom"
import {Counter} from 'counter/index'
import { Login, Signup, UserDetail, UserEdit, UserList} from 'user/index'
import {Home} from 'common/index'


const App = () => {
  return (<div>
    <Route exact path='/' component={Home}/>
    <Route exact path='/counter' component={Counter}/>
    <Route exact path='/login' component={Login}/>
    <Route exact path='/Signup' component={Signup}/>
    <Route exact path='/user-detail' component={UserDetail}/>
    <Route exact path='/user-edit' component={UserList}/>
    <Route exact path='/user-list' component={UserEdit}/>
  </div>)
 
}

export default App