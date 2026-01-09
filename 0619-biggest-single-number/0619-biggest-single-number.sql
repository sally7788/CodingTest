# Write your MySQL query statement below
#한번만 등장하는 숫자 중 가장 큰 값 

select max(num) as num
from (select num 
    from MyNumbers
    group by num 
    having count(num) = 1) t
