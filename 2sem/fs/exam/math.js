var http = require('http');
var cm=require('./cal');

http.createServer(function(req,res){
    res.writeHead(100,{'Content-Type':'text/html'});
    res.write('Add:'+cm.add(25,50)+'</br>');
    res.write('Sub:'+cm.sub(25,50)+'</br>');
    res.write('Mul:'+cm.mul(25,50)+'</br>');
    res.write('Div:'+cm.div(25,50)+'</br>');
}).listen(4200,console.log("server running at port 4200"));