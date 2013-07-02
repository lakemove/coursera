--select cr, cc, sum(cv) from 
select sum(cv) from
(select ar cr, bc cc, av*bv cv from
  (select a.row_num ar, a.col_num ac, a.value av,
    b.row_num br, b.col_num bc, b.value bv
   from a, b where a.col_num=b.row_num)
 ) group by cr, cc
having cr=2 and cc=3
;
