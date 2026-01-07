# Write your MySQL query statement below
-- with salary_num as (
--     select salary, dense_rank() over (order by salary desc) as num
--     from employee )

-- select max(salary) as SecondHighestSalary
-- from salary_num
-- where num = 2 

select (
    select distinct salary 
from employee 
order by salary desc 
limit 1 offset 1) as SecondHighestSalary;