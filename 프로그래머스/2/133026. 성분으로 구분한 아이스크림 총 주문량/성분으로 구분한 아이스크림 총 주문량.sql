select i.ingredient_type, sum(f.total_order) as total_order
from first_half f, icecream_info i
where f.flavor = i.flavor
group by i.ingredient_type
order by total_order asc