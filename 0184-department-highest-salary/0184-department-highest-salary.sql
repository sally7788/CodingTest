# Write your MySQL query statement below
with salary_number as ( 
    select d.name as Department, e.name as Employee, salary as Salary,
    dense_rank() over (partition by DepartmentID order by salary desc) as number
    from employee e 
    join department d on e.departmentId = d.id )

select Department, Employee,Salary
from salary_number 
where number = 1;