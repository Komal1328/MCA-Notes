var express = require('express');
var app = express();
app .get('/',function(req,res){
    console.log("Got get request");
    res.send("Welcome to express");
})
app.post('/',function(req,res){
    res.send('Hiii');
})
app .get('/enroll_student',function(req,res){
    console.log("Got get request");
    res.send("enroll");
})
app .get('/ab*bd',function(req,res){
    console.log("Got get request");
    res.send("pattern match");
})

var server = app.listen(4200,function(){
    var host = server.address().address
    var port=server.address().port
    console.log("Example app listening at http://%s:%s",host,port)
})