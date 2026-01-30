with cond as (SELECT distinct car_id

from car_rental_company_rental_history

where '2022-10-16' between start_date and end_date)



select distinct car_id, 

if(car_id in (select car_id from cond), '대여중', '대여 가능') as availability

from CAR_RENTAL_COMPANY_RENTAL_HISTORY

order by car_id desc;