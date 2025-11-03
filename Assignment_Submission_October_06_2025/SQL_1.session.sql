SELECT p.category,
    SUM(s.quantity_sold) AS total_units_sold,
    SUM(s.sale_amount) AS total_revenue
FROM Sales s
    INNER JOIN Products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;