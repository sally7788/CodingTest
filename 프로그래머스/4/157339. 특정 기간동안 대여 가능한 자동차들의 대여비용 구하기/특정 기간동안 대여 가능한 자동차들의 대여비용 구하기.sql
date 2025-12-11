-- 코드를 입력하세요

with CTE as (
select round((1-DISCOUNT_RATE/100)*DAILY_FEE*30) as fee, c.car_id
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
join CAR_RENTAL_COMPANY_CAR c on p.CAR_TYPE=c.CAR_TYPE
where DURATION_TYPE='30일 이상')


SELECT c.car_id, c.car_type, t.fee
from (select car_id, car_type
     from CAR_RENTAL_COMPANY_CAR 
     where CAR_TYPE in ('세단', 'SUV')) c
join CTE t on t.car_id =  c.car_id
where t.fee between 500000 and 2000000
     and c.car_id not in (
         select car_id
         from CAR_RENTAL_COMPANY_RENTAL_HISTORY
         where END_DATE >= '2022-11-01' and START_DATE <= '2022-11-30' )
order by 3 desc, 2, 1 desc