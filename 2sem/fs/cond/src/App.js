import React, { useRef } from 'react';
import './App.css';
export default function Uncontrolled(){
  const in1 = useRef(null);
  const in2 = useRef(null);
  const in3 = useRef(null);

  function handleSubmit(){
    const res=0;
    if(in3.current.value==='+')
      res=in1.current.value+in1.current.value;
      alert(`Result: ${res}`);
    
  }
  return(
    <div className='app'>
      <h1>Hi welcome to forms</h1>
      <form onSubmit={handleSubmit}>
        <label>Number1
          <input type='text' name="no1" ref={in1}/>
        </label><br/>
        <label>Number2
          <input type='text' name="no2" ref={in2}/>
        </label><br/>
        <label>Operator
          <input type='text' name="no1" ref={in3}/>
        </label><br/>
        <button type='submit' value="submit">Submit</button>
      </form>       
    </div>
  );
}
