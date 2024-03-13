import {useState} from 'react';

function App() {
  const [name, setname] = useState('');
  const [email, setEmail] = useState('');

function onSubmit() {
  console.log("Name value: "+name);
  console.log("Email value: "+email);
}
function onRest(){
  window.location.reload(false);
}
return (
  <form onSubmit={onSubmit}>
    <label>Name:</label>
    <input type='text' name='name' value={name} onChange= {(e) => setname(e.target.value)} required/><br/>
    <label>Email:</label>
    <input type='text' name='email' value={email} onChange= {(e) => setEmail(e.target.value)} required/><br/>
    <input type='submit' value="submit"/> 
    <input type='reset' value="reset" onClick={onRest}/>
  </form>
);
}
export default App;