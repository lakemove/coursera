select fr1.term from frequency fr1 where fr1.docid='10398_txt_earn' and fr1.count=1 
union
select fr2.term from frequency fr2 where fr2.docid='925_txt_trade' and fr2.count=1 
;