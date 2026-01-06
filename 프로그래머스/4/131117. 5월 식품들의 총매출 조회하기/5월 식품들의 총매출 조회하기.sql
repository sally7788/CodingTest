-- 코드를 입력하세요
SELECT p.product_id, product_name, sum(amount)*price as total_sales
from food_product p
join food_order o on p.product_id = o.product_id 
and date_format(o.produce_date, "%Y-%m")='2022-05'
group by 1,2
order by 3 desc, 1