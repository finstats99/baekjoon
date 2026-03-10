select MCDP_CD as '진료과코드', count(PT_NO) as '5월예약건수'
from appointment
where (apnt_ymd like '2022-05%')
group by MCDP_CD
order by 5월예약건수, 진료과코드

# SELECT MCDP_CD AS '진료과 코드', COUNT(PT_NO) AS '5월예약건수'
# FROM APPOINTMENT
# WHERE APNT_YMD LIKE '2022-05%'
# GROUP BY MCDP_CD
# ORDER BY 5월예약건수 ASC, MCDP_CD ASC;