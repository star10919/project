import React, { useState } from 'react'

const Todo = () => {
    const [item, setItem] = useState('')

    return (<>
    <h1> 할일 목록 </h1>
    <h4>{item}</h4>

    <input onChange = { e => setItem(e.target.value) }/> <br/> <br/>
    <button onClick = { () => {setItem( '' )}}> 할일추가 </button>
    <button onClick = { () => {setItem( '' )}}> 초기화 </button>
    
    </>)
}

export default Todo