-- 코드를 작성해주세요
select  id,fish_name, length
from FISH_INFO f
join FISH_NAME_INFO n on f.FISH_TYPE=n.FISH_TYPE
where (f.FISH_TYPE, length) in 
    (select fish_type, max(length)
     from FISH_INFO 
     group by fish_type)
order by 1
