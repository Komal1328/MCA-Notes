var http=require("http");
	http.createServer(function(request,response){
	response.writeHead(200,{'content-Type':'text/plain'});
	response.write("Hello World\n");
	response.end();
}).listen(8087);

console.log("Running at url http://localhost:8087/");

