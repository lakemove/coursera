
var fs = require('fs')
  , crypto = require('crypto')
  ;

fs.readFile('test.csv', function (err2, data2) {
	var lines = data2.toString().split('\n').slice(1);
	fs.readFile('result3', function (err, data) {
		var ps = data.toString().split('\n');
		for (var i = 0; i < lines.length; i++) {

			var psi = ps[i], linei = lines[i];
			var p = psi.substring(2, 4);
			var action = ((p - 0) < 25 ) ? 0 : 1;
			console.log(action + ',' + linei.substring(linei.indexOf(',') + 1));
		}
	});
});
