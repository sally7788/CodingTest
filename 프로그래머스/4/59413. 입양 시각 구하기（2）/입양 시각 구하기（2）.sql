-- 코드를 입력하세요
with recursive time as (
    select 0 as n
    union all 
    select n+1 
    from time
    where n < 23)

select t.n as hour, ifnull(count,0) as count
from (select count(*) as count, date_format(datetime, '%H') as hour
from animal_outs 
group by date_format(datetime, '%H')) a
right join time t on a.hour=t.n
