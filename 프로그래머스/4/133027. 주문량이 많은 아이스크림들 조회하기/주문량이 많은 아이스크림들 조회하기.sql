-- 코드를 입력하세요
with Torder as (
    SELECT flavor, total_order
    from first_half 
    union all 
    SELECT flavor, total_order
    from july
)


select flavor
from (
    select flavor, sum(total_order)
    from Torder
    group by flavor
    order by 2 desc
    limit 3
) as f