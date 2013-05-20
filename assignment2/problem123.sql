
-- attach
ATTACH DATABASE 'reuter.db' As 'reuter';

-- display attached database
.database

-- detach
DETACH DATABASE 'reuter';

-- show tables
.tables
-- reuter.Frequency

-- select
SELECT * FROM FREQUENCY;

-- a) select
SELECT * FROM Frequency WHERE docid == '10398_txt_earn';
SELECT count(*) FROM Frequency WHERE docid == '10398_txt_earn';
count(*)
----------
138

-- b) slect project
SELECT term FROM Frequency WHERE docid == '10398_txt_earn' AND count == 1;
SELECT count(term) FROM Frequency WHERE docid == '10398_txt_earn' AND count == 1;
count(term)
-----------
110

-- c) union
select count(*) FROM (
SELECT term FROM Frequency WHERE docid == '10398_txt_earn' AND count == 1
UNION 
SELECT term FROM Frequency WHERE docid == '925_txt_trade' AND count == 1);
count(*)
----------
324


-- d) count
SELECT docid FROM Frequency WHERE term == 'parliament';
SELECT count(docid) FROM Frequency WHERE term == 'parliament';
count(docid)
------------
15

-- e) big documents
big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
SELECT count(*) FROM (
SELECT * FROM Frequency 
GROUP BY docid
HAVING sum(count) > 300);
count(*)
----------
107

-- f) two words
Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
SELECT count(*) FROM 
(SELECT docid FROM Frequency WHERE term == 'transactions') AS QA
INNER JOIN 
(SELECT docid FROM Frequency WHERE term == 'world') AS QB
ON QA.docid = QB.docid ;
count(*)
----------
3

-- g) multiply
SELECT A.row_num, B.col_num, SUM(A.value*B.value) as value
FROM A, B
WHERE A.col_num = B.row_num
GROUP BY A.row_num, B.col_num;


-- h)
-- compute the similarity matrix DDT
SELECT A.docid, B.docid, SUM(A.count * B.count) as similarity
FROM frequency as A, frequency as B
WHERE A.term = B.term and A.docid < B.docid
GROUP BY A.docid, B.docid;

select a.docid, a.term, b.term, sum(a.count * b.count) as similarity
from frequency a, frequency b
where a.docid = "10080_txt_crude" and b.docid = "17035_txt_earn" and a.term = b.term
group by a.docid

SELECT A.docid, B.docid, SUM(A.count * B.count) as similarity
FROM frequency as A, frequency as B
WHERE A.docid = "10080_txt_crude" AND B.docid = "17035_txt_earn" AND A.term = B.term AND A.docid < B.docid
GROUP BY A.docid, B.docid;


-- i) keyword search
SELECT A.docid, B.docid, SUM(A.count * B.count) as similarity
FROM frequency as A, 
(
  SELECT 'q' as docid, 'washington' as term, 1 as count 
  UNION
  SELECT 'q' as docid, 'taxes' as term, 1 as count
  UNION 
  SELECT 'q' as docid, 'treasury' as term, 1 as count
) as B
WHERE A.term = B.term AND A.docid < B.docid
GROUP BY A.docid, B.docid
ORDER BY similarity DESC
limit 10;

