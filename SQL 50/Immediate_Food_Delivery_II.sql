SELECT ROUND(SUM(CASE WHEN order_date=customer_pref_delivery_date THEN 1 ELSE 0 END)/COUNT(Delivery.customer_id) *100.0,2) as immediate_percentage
FROM Delivery
LEFT JOIN 
(
    SELECT customer_id, MIN(order_date) as order1
    FROM Delivery
    GROUP BY customer_id
) AS Order1 ON Delivery.customer_id=Order1.customer_id
WHERE order_date=order1;


-- -boolean returs can be evaluated as 1 / 0
-- -replace SUM(CASE WHEN boolean_conditional THEN 1 ELSE 0 END)/COUNT(Delivery.customer_id) with
-- -AVG(boolean_conditional)*100

-- -ALTERNATIVE SOLUTION
Select 
    round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);
