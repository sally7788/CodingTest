-- 코드를 입력하세요
select food_type, rest_id, rest_name, favorites
from (
    SELECT food_type, rest_id, rest_name, favorites,
    row_number() over (partition by food_type order by favorites desc) as ranking
from rest_info
) r
where ranking=1
order by food_type desc 