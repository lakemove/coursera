select abc from 
(select ad , sum(ac * bc) abc from 
	(select a.docid ad, a.term at, a.count ac, b.docid bd, b.term bt, b.count bc from 
		(select docid, term, count from frequency ) a, 
		(SELECT 'q' as docid, 'washington' as term, 1 as count UNION SELECT 'q' as docid, 'taxes' as term, 1 as count UNION SELECT 'q' as docid, 'treasury' as term, 1 as count) b where a.term = b.term) group by ad order by abc desc limit 1)
;
