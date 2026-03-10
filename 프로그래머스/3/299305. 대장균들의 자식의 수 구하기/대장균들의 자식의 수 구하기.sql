select e1.id, count(e2.id)
from ecoli_data e1, ecoli_data e2  
where e1.id = e2.parent_id   # e2가 자식
group by e1.id