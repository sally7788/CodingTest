-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y') year, date_format(sales_date, '%m') month, gender,count(distinct i.user_id) users
from (select USER_ID, GENDER
     from USER_INFO 
     where gender is not null) i
join ONLINE_SALE s on i.user_id = s.user_id
group by date_format(sales_date, '%Y'), date_format(sales_date, '%m'), gender
order by 1,2,3