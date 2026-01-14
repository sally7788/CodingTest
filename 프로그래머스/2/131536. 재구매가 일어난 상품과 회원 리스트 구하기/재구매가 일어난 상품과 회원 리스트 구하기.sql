-- 코드를 입력하세요
SELECT user_id, product_id
from online_sale a
group by user_id, product_id
having count(*) >=2
order by 1, 2 desc
    