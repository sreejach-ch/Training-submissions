-- 1️⃣ View all sales
SELECT * FROM fact_sales;

-- 2️⃣ Get monthly sales by category
SELECT 
    d.year,
    d.month_name,
    p.category,
    SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY d.year, d.month_name, p.category
ORDER BY d.year, d.month_name;

-- 3️⃣ Find top customers by total spend
SELECT 
    c.customer_name,
    SUM(f.total_amount) AS total_spent
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
