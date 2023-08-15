SELECT Visits.customer_id, COUNT(customer_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions on Visits.visit_id=Transactions.visit_id
WHERE transaction_id is null
GROUP BY customer_id;

-- OR -- -

SELECT Visits.customer_id, COUNT(customer_id) as count_no_trans
FROM Visits
WHERE visit_id NOT in 
  (SELECT visit_id FROM Transactions)
GROUP BY customer_id;
