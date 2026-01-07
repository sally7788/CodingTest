# Write your MySQL query statement below
#적어도 3번 이상 반복되어 나오는 숫자 
with num_order as (
select id, num, lag(num, 1) over (order by id) as prev, lead(num,1) over (order by id) as next 
from logs )

select distinct num as ConsecutiveNums
from num_order 
where num=prev and num=next
