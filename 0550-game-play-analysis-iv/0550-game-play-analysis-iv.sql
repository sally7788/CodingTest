# Write your MySQL query statement below
-- 처음 로그인한 날 이후로 다시 로그인한 플레이어의 조각 
-- 처음 로그인을 따라간 날에 로그인한 플레이어의 수? 뭔말이야 그걸 전체 회원 수로 나눠라 
-- 아 처음 로그인하고 다음날에 다시 로그인한 플레이어가 몇명이냐고 

with new as (
    select player_id, min(event_date) as event_date
    from activity
    group by player_id)

select round(count(a.player_id)*1.0/count(n.player_id),2) as fraction
from new n
left join activity a on n.player_id = a.player_id 
    and datediff(a.event_date, n.event_date)=1

