
var fs = require('fs')
  , crypto = require('crypto')
  ;

fs.readFile('train.csv', function(err, data) {
  var lines = data.toString().split('\n').slice(1);

  var t = [{}, {}, {}, {}, {}, {}, {}, {}, {}];
  lines.forEach(function (line, idx) {
    var cols = line.split(',');
    for (var i = 1; i < 10; i++) {
      if (! t[i-1][cols[i]]) {
        t[i-1][cols[i]] = {c : 0, s : 0};
      }
      var a = t[i-1][cols[i]];
      t[i-1][cols[i]] = {c : a.c + 1, s : a.s + (cols[0] - 0)};
    }
  });

  fs.readFile('test.csv', function (err2, data2) {
    var lines = data2.toString().split('\n').slice(1);
    lines.forEach(function (line) {
      var cols = line.split(',');
      var p = 0.99;
      for (var i = 1; i < 10; i++) {
        var hist = t[i - 1][cols[i]];
        if (hist && hist.c) {//no appear in history
          if (hist.s == 0) {
            p = p * 0.01;
          }else {
            p = p * (hist.s/hist.c);
          }
        }
      }
      if ( p < 0.25) {
        console.log(cols[0] + ',0');
      } else {
        console.log(cols[0] + ',1');

      }
    });
  });
});
/*
fs.readFile('train.csv', function(err, data) {
  var lines = data.toString().split('\n');

  var rolehash = {};
  lines.slice(1).forEach(function (line) {
    var cols = line.split(',');
    var action = cols[0], resource = cols[1], role = cols.slice(3);
    var h = role.join(',');
    rolehash[h] = role;
  });
  var counter = 0;
  var uniq_roles = [];
  for (x in rolehash) {uniq_roles.push(x.split(','));};
  console.log("all roles count : " + uniq_roles.length);

  var matrix = []; 
  var tmp = '', count = 0;
  for (var i = 0; i < uniq_roles.length; i++) {
    var a = uniq_roles[i], aj = a.join(',');
    count++;  
    for (var j = i; j < uniq_roles.length; j++) {
      count++;
      var b = uniq_roles[j], bj = b.join(',');
      var v = similarity(a, b);
      tmp += aj + '|' + bj + '|' + v + '\n';
      if(count % 300 == 0) {
        fs.appendFileSync('/tmp/matrix', tmp);
        count = 0; tmp = '';
      }
      
      // matrix.push({a : aj, b : bj, v : v});
    }
    console.log(i);
  }
  fs.appendFileSync('/tmp/matrix', tmp);


});

function hash (str) {
  var md5 = crypto.createHash('md5');
  md5.update(str);
  return md5.digest('hex');
}

function similarity (a, b) {//similarity of role a and role b
  var c = 0;
  a.forEach(function(item, idx) {
    c += item == b[idx] ? 1 : 0;
  });
  return c/a.length;
}

*/