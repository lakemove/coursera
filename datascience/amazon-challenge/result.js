
var fs = require('fs')
  , crypto = require('crypto')
  ;

fs.readFile('result2', function(err, data) {
  var lines = data.toString().split('\n').slice(1);
  var stat = {};
  lines.forEach(function (line) {
    if(!stat[line[2]]) {
      stat[line[2]] = 1;
    } else {
      stat[line[2]] += 1;
    }
  });

  for (var i in stat) {
    console.log(i + ' : ' + stat[i]);
  }

});
