var http=require('http');
var dt=require('./module');

http.createServer(function(req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    res.write("The date and time are currently"+dt.myDateTime());
    res.end();
}).listen(4200,console.log("server running at port 4200"));

