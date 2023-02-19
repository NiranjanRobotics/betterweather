
const express = require("express");
const fs = require("fs");


const PORT = process.env.PORT || 8080;

const app = express();

app.get("/api", (req, res)=>{
    res.json({message: "hello from server"});
    // console.log("getting the info hopefully")
    // console.log(req);
    // console.log(res);
});

app.post("/post", (req, res) => {
    console.log("Connected to React");
    res.redirect("/");
  });


app.listen(PORT, ()=>{console.warn("Server listening on port: " + PORT)});

// app.listen(PORT, ()=>{
//     console
// })
