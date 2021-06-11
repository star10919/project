import React from 'react'
import { TodoMenu as Menu } from '../common'
import './table.style.css'

const Todos = (children) => (<>
    <h1>Todos</h1>
    <Menu/>
    {children}
</>)

export default Todos