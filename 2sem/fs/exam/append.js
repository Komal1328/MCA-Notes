var fs = require('fs');

fs.appendFile('text.txt','MCA Department!',function(err){
    if(err)
        console.log(err);
    else
        console.log("Append");
});