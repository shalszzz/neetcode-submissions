-- Write your query below
select * from customers c where c.customer_id IN (select customer_id from orders where product_name='A')
AND c.customer_id IN (select customer_id from orders where product_name='B')
AND c.customer_id NOT IN (select customer_id from orders where product_name='C')
order by customer_name;