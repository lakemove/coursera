
var fs = require('fs')
  , crypto = require('crypto')
  ;

fs.readFile('test.csv', function (err2, data2) {
	var lines = data2.toString().split('\n').slice(1);
	console.log(lines.length);
	console.log(lines[0]);
	console.log(lines[lines.length - 1]);
});
