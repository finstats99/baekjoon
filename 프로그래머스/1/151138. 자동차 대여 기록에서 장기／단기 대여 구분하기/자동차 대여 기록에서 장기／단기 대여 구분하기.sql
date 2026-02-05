SELECT  history_id
        , car_id
        , date_format(start_date, '%Y-%m-%d') as start_date
        , date_format(end_date, '%Y-%m-%d') as end_date
        , if(datediff(end_date, start_date) + 1 >= 30, '장기 대여', '단기 대여') as rent_type
  FROM  CAR_RENTAL_COMPANY_RENTAL_HISTORY
 WHERE  MONTH(start_date) = 9
 order
    by  history_id desc