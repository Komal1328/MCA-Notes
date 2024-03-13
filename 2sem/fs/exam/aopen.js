var fs= require('fs');

console.log('Opening file');
fs.open('input.txt','r+',function(err){
    if(err){
        return console.error(err);
    }
    console.log('opened')
})