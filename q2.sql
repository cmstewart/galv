select s.name
from orders o, salesperson s
where o.salesperson_id = s.id
group by o.salesperson_id
having count(o.salesperson_id) > 1