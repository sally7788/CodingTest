# Write your MySQL query statement below
#친구수 구하고, 친구 가장 많은 사람 

select id, count(id) as num
from (select accepter_id as id
    from requestAccepted
    union all 
    select requester_id as id
    from requestAccepted
    ) t
group by id
order by num desc
limit 1


