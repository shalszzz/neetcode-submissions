-- Write your query below

select employee_id, salary as bonus 
from employees
where MOD(employee_id,2)=1
AND name not like 'M%'

UNION 

select employee_id, 0 as bonus
from employees
where MOD(employee_id,2)=0
OR name like 'M%'

order by employee_id;