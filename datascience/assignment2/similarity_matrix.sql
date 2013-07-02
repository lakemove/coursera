

select count(*) from 
  (select a.docid ar, a.term ac, a.count av, b.docid br, b.term bc, b.count bv from frequency a, frequency b)
;