import React, { useState, useEffect } from "react";
import "./Post.css";

function Post({ post }) {
  
  const [imageUrl, setImageUrl] = useState("");
  const [comments, setComments] = useState([]);

  useEffect(() => {
    setImageUrl(post.image_url);
  }, []);

  useEffect(()=>{
    setComments(post.comments)
  }, [])
  return (
    <div className="post">
      <img className="post_image" src={imageUrl} />
      <h4 className="post_label"> {post.caption} </h4>  
      <div className="post_comments"> {comments.map(comment=> (
      <p> {comment.username}: {comment.text} </p>
      ))} 
      </div>
    </div>
  );
}

export default Post;
