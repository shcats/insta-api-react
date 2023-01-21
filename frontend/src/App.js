import "./App.css";
import React, { useState, useEffect } from "react";
import Post from "./Post";

const BASE_URL = "http://127.0.0.1:8000";

function App() {
  const [posts, setPost] = useState([]);

  useEffect(() => {
    fetch(BASE_URL + "/post/all")
      .then((response) => {
        const json = response.json();
        console.log(json);
        if (response.ok) {
          return json;
        }
      })
      .then((data) => {
        setPost(data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <div className="app_posts">
      {posts.map((post) => (
        <Post post={post} />
      ))}
    </div>
  );
}

export default App;
