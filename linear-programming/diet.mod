# STIGLER'S NUTRITION MODEL
#
# This model determines a least cost diet which meets the daily
# allowances of nutrients for a moderately active man weighing 154 lbs.
#
#  References:
#              Dantzig G B, "Linear Programming and Extensions."
#              Princeton University Press, Princeton, New Jersey, 1963,
#              Chapter 27-1.

set N;
/* nutrients */

set F;
/* foods */

param b{N};
/* minimum allowed nutrients */

param bb{N};
/* maximum allowed nutrients */

param a{F,N};
/* nutritive value of foods (per dollar spent) */

var x{f in F} >= 0;
/* dollars of food f to be purchased daily */

s.t. nb{n in N}: sum{f in F} a[f,n] * x[f] * (-1) <= (-1) * b[n];
s.t. nbb{n in N}: sum{f in F} a[f,n] * x[f] <= bb[n];
/* nutrient balance (units) */

minimize cost: sum{f in F} x[f];
/* total food bill (dollars) */

data;

param : N : b : bb :=
         Carbs    100 1000  
         Protein  10  100
         Fat      0   100 ;

set F := Carbs Protein Fat Price;

param a default 0

:             Carbs   Protein   Fat    Price  :=  
#            (1000)    (g)      (g)    ($) 
Rice         53       4.4       0.4    0.5  
Quinoa       40       8         3.6    0.9  
Tortilla     12       3         2      0.1
Lentils      53       12        0.9    0.6  
Broccoli     6        1.9       0.3    0.4    ;   

end;
