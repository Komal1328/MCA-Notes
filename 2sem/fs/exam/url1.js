var express = require('express');
var app = express();

app.get('/:name/:id',function(req,res){
    res.send("id is"+req.params.id+'and name '+req.params.name);
});
app.listen(4200);