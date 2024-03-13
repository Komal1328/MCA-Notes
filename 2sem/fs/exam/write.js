var fs = require('fs');

fs.writeFile('text.txt','Hello world!',function(err){
    if(err)
        console.log(err);
    else    
        console.log("Success");
});