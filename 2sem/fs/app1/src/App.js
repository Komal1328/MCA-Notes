import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="Example">
      <h1>Hi welcome to forms</h1>
      <form className='example'>
      <fieldset>
        <label>Name</label>
        <input type='text'></input>
      </fieldset>
      <button type='submit' value="submit">Submit</button>
      </form>       
    </div>
  );
}

export default App;