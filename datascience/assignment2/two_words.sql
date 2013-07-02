select docid from frequency where term='transactions'
  and docid in (select f2.docid from frequency f2 where f2.term='world')
;