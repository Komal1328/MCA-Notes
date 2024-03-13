var fs=require('fs');
var data=fs.readFileSync('input1.txt',function(err){
    if(err)
        console.log(err)
    else
    console.log(data.toString());
});
console.log("program end!!!!!!!");
