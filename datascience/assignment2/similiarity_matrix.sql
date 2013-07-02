
select sum(ac * bc) abc from 
	(select a.docid ad, a.term at, a.count ac, b.docid bd, b.term bt, b.count bc from 
		(select docid, term, count from frequency where docid='10080_txt_crude') a, 
		(select docid, term, count from frequency where docid='17035_txt_earn') b where a.term = b.term) group by ad
-- (select b.docid, b.term, b.count from frequency b where b.docid='17035_txt_earn')

;