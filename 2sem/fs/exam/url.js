var http = require('http');
http.createServer(function(req,res){
    // res.writeHead(200,{'Content-type':'text/html'});
    res.write(req.url);
    res.end();
}).listen(4200,console.log("server running at port 4200"));