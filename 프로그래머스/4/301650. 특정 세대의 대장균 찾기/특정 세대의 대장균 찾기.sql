select e3.id
from (select e2.id  # 2세대 id를 출력으로)
        from ecoli_data e1 # e1.id : 1세대 id
        join ecoli_data e2 on e1.id = e2.parent_id
        where e1.parent_id is null) e2
        # 2세대 id와 3세대 parent_id연결
join ecoli_data e3 on e2.id = e3.parent_id

# select e1.id, e2.id  # 2세대 id를 출력으로)
# from ecoli_data e1 # e1.id : 1세대 id
# join ecoli_data e2 on e1.id = e2.parent_id
# where e1.parent_id is null