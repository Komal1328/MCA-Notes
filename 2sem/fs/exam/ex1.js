var express = require('express');
var app=express();

app.get('/hello',function(req,res){
    res.send("hello world");
});
app.listen(4200);
console.log("runjing at 4200");