var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x0 >= 0;

#minimize obj: 0.5 * x1 + 0.9 * x2 + 0.1 * x3 + 0.6 * x4 + 0.4 * x5;
maximize obj: -x0;
c1: -x1 - x2 - x0 <= 5;
c2: x1 - 2*x2 + x3 - x0 <= -10;
c3: x1 - x3 - x0 <= -20;
c4: x1 + x2 + x3 - x0 <= 3;

solve;
display x0;
#display 0.5 * x1 + 0.9 * x2 + 0.1 * x3 + 0.6 * x4 + 0.4 * x5;
end;