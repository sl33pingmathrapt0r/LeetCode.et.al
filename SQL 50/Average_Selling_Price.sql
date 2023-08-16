SELECT product_id, ROUND(SUM(Sales.sales)/SUM(Sales.units),2) AS average_price
FROM
(
    SELECT UnitsSold.product_id, units, price*units as sales
    FROM UnitsSold
    LEFT JOIN Prices ON UnitsSold.product_id=Prices.product_id AND DATEDIFF(purchase_date, start_date)>=0 AND DATEDIFF(purchase_date, end_date)<=0
) AS Sales
GROUP BY product_id;
