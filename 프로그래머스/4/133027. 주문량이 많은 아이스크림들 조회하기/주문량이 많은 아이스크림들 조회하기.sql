-- 코드를 입력하세요
with half_order as (
    SELECT flavor, sum(total_order) as total_order
    from first_half 
    group by flavor
),

july_order as (
    select flavor, sum(total_order) as total_order
    from july
    group by flavor)

select flavor
from (
    select h.flavor, h.total_order+j.total_order as real_total
    from half_order h
    join july_order j on h.flavor=j.flavor
    order by real_total desc
    limit 3
) as f