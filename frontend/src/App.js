import "./App.css";
import React, { useState, useEffect } from "react";
import Post from "./Post";
import { Button, Modal } from "@mui/material";
import { makeStyles } from "@mui/styles";

const BASE_URL = "http://127.0.0.1:8000";

function getModalStyle(){
  const top=50;
  const left=50;
  return {
    top:`${top}%`,
    left:`${left}%`,
    transform:`translate(-${top}%, -${left}%)`
  }
}

const useStyles = makeStyles((theme)=>({
  paper: {
    backgroundColor: 'white',
    position: 'absolute',
    width: 400,
    border: '2px solid #000',
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
    padding: '8px 16px 24px',
  },
}));

function App() {
  const classes = useStyles()

  const [posts, setPost] = useState([]);
  const [openSignIn, setopenSignIn] = useState(false)
  const [openSignUp, setopenSignUp] = useState(false)
  const [modalStyle, setModalStyle] = useState(getModalStyle)

  useEffect(() => {
    fetch(BASE_URL + "/post/all")
      .then((response) => {
        const json = response.json();
        console.log(json);
        if (response.ok) {
          return json;
        }
        throw response
      })
      .then(data=>{
        const result = data.sort((a,b)=>{
          const t_a = a.timestamp.split(/[-T:]/)
          const t_b = b.timestamp.split(/[-T:]/)
          const d_a = new Date(Date.UTC(t_a[0], t_a[1] - 1, t_a[2], t_a[3], t_a[4], t_a[5]));
          const d_b = new Date(Date.UTC(t_b[0], t_b[1] - 1, t_b[2], t_b[3], t_b[4], t_b[5]));
          return d_b - d_a
        })
        return result
      })
      .then((data) => {
        setPost(data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <div className="app">

     <Modal open={openSignIn} onClose={()=>setopenSignIn(false)}>

        <div style={modalStyle} className={classes.paper}></div>

      </Modal>
    
      <div className="app_header">
        <img className="app_headerImage" 
          src="https://png.monster/wp-content/uploads/2020/11/Instagram-zeichen_2-2c204007.png" 
          alt=""/>
        <div>
        <Button onClick={()=>setopenSignIn(true)}> LOGIN</Button>
        <Button onClick={()=>setopenSignUp(true)}> SIGNOUT</Button> 
      </div>
      </div>
      <div className="app_posts">
        {posts.map((post) => (
          <Post post={post} />
        ))}
      </div>
    </div>
  );
}

export default App;
