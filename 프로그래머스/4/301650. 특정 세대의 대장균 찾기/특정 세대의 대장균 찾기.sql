with cond as (select a.id, b.parent_id, b.id as sibling_id
from ecoli_data a, ecoli_data b
where b.parent_id = a.id and a.parent_id is null)  # sibling_id : 2세대 부모역할

select c.id
from ecoli_data c, cond
where c.parent_id = cond.sibling_id # c.id : 3세대 (2세대의 자식)
order by c.id