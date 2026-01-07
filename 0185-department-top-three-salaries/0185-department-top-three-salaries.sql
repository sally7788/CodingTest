# Write your MySQL query statement below
#각 부서에서 누가 가장 돈을 많이 버나..
#한 부서의 고소득자는 탑쓰리 유니크한 월급을 가진다. -> 부서당 가장 높은 월급 3가지만 들어갈 수 잇나보다. 그런데 같은 월급 받는 사람 있으면 포함됨 
#각 부서에서 고소득자를 찾는 방법

with salary_number as (
    select d.name as Department, e.name as Employee, salary,
    dense_rank() over (partition by e.departmentid order by salary desc) as number
    from employee e
    join department d on e.departmentid = d.id
)

select department, employee, salary
from salary_number
where number<= 3
order by salary desc

