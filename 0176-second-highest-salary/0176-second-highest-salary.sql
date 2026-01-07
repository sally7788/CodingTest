# Write your MySQL query statement below
with salary_num as (
    select salary, dense_rank() over (order by salary desc) as num
    from employee )

select max(salary) as SecondHighestSalary
from salary_num
where num = 2 
