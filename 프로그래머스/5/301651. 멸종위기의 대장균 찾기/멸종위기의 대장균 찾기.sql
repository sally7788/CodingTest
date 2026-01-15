-- 코드를 작성해주세요
with recursive ecoli as (
    select id, parent_id, 1 as generation
    from ecoli_data 
    where parent_id is null
    
    union all
    
    select e1.id, e1.parent_id, e2.generation+1
    from ecoli_data e1
    join ecoli e2 on e1.parent_id = e2.id
)

select count(*) as count,generation
from ecoli e1
where not exists (
select 1
from ecoli e2
where e1.id = e2.parent_id)
group by generation
order by generation