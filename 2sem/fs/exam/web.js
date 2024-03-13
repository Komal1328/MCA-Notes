var http = require('http');
var fs = require('fs');

http.createServer(function(req,res){
    fs.readFile('input.txt',function(err,data){
        res.write(data);
        return res.end();
    });
}).listen(4200,console.log("running ar 4200"));