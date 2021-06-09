import React from 'react'
import { TodoInput, TodoList } from '../components'
import { store } from '../store'
import { Provider } from 'react-redux'

const Schedule = () => {
    return (<>
    <Provider store={store}>
        <TodoInput/>
        <TodoList/>
    </Provider>
    </>)
}

export default Schedule