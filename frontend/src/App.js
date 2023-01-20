import './App.css';
import React, {useState, useEffect} from 'react';


const BASE_URL = "http://127.0.0.1:8000"

function App() {

  const [post, usePost] = useState([])


  useEffect(() => {
    
    fetch(BASE_URL + "/post/all")
    .then((response)=>{
      console.log(response.json());
    })
    .then()

  }, [])
  

  return (
    <div className="App">
      <p> Hekko</p>
    </div>
  );
}

export default App;
