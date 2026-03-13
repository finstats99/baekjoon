select car_type, count(car_id) as cars
from car_rental_company_car
WHERE OPTIONS LIKE '%통풍시트%'
   OR OPTIONS LIKE '%열선시트%'
   OR OPTIONS LIKE '%가죽시트%'
group by car_type
order by car_type