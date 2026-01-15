-- 코드를 입력하세요

with avaliable as (
    select c.car_id, car_type, daily_fee
    from CAR_RENTAL_COMPANY_CAR c
    where car_type in ('세단', 'SUV')
    and car_id not in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where start_date <= '2022-11-30' and end_date >= '2022-11-01')
)
select car_id, car_type, round(total_fee,0) as fee
from (
    select a.car_type, car_id, (1-discount_rate/100)*daily_fee*30 as total_fee
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    join avaliable a on a.car_type = p.car_type  and duration_type='30일 이상') as f
where total_fee >= 500000 and total_fee <= 2000000
order by fee desc, car_type, car_id desc
    
    
