# Write your MySQL query statement below
#전날보다 온도가 높은 날짜 찾기 id 출력

select w2.id
from Weather w1
join Weather w2 on datediff(w2.recorddate, w1.recorddate) = 1
and w2.temperature > w1.temperature 
