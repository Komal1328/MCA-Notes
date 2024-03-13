var fs = require('fs');

fs.unlink('test.txt',function(err){
    if (err)
        console.log(err);
    else
        console.log("deleted");
});