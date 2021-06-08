import { Counter, Todo } from './components/index'
import { Route } from 'react-router-dom'


const App = () =>{
  return <div>
    <Route exact path='/' component={ Counter }/>
    <Route exact path='/todo' component={ Todo }/>
  </div>
}

export default App