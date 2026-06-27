SELECT COUNT(*)
FROM orders_clean;
SELECT COUNT(*)
FROM products_clean;
SELECT COUNT(*)
FROM order_items_dataset_clean;

SELECT COUNT(*)
FROM valid_orders;

SELECT *
FROM gmv_base
LIMIT 5;

SELECT *
FROM user_base
LIMIT 5;

SELECT *
FROM feature_order
LIMIT 10;

SELECT *
FROM feature_customer_lifecycle
LIMIT 10;

SELECT *
FROM feature_repurchase_interval
WHERE repurchase_interval_days IS NOT NULL
LIMIT 20;

SELECT COUNT(*) FROM feature_order;

SELECT AVG(order_total_amount)
FROM feature_order;

SELECT AVG(delivery_days)
FROM feature_order;

SELECT AVG(lifecycle_days)
FROM feature_customer_lifecycle;

SELECT *
FROM monthly_base
LIMIT 10;

SELECT
    month,
    ROUND(SUM(price),2) AS GMV
FROM monthly_base
GROUP BY month
ORDER BY month;

SELECT
    month,
    COUNT(DISTINCT order_id) AS order_cnt
FROM monthly_base
GROUP BY month
ORDER BY month;

SELECT
    month,
    COUNT(DISTINCT customer_id) AS user_cnt
FROM monthly_base
GROUP BY month
ORDER BY month;

SELECT
    month,

    ROUND(
        SUM(price)
        /
        COUNT(DISTINCT order_id),
        2
    ) AS AOV

FROM monthly_base

GROUP BY month

ORDER BY month;

SELECT

    month,

    gmv,

    LAG(gmv)
    OVER(
        ORDER BY month
    ) AS last_month,

    ROUND(

        (
            gmv
            -
            LAG(gmv)
            OVER(
                ORDER BY month
            )
        )

        *100.0

        /

        LAG(gmv)
        OVER(
            ORDER BY month
        )

    ,2)

AS mom_growth

FROM monthly_dashboard;

SELECT

    month,

    gmv,

    order_cnt

FROM monthly_dashboard

WHERE month LIKE '%-11'

OR month LIKE '%-12';

SELECT *
FROM payment_analysis;

SELECT

CASE

WHEN amount<50 THEN '0-50'

WHEN amount<100 THEN '50-100'

WHEN amount<200 THEN '100-200'

WHEN amount<500 THEN '200-500'

ELSE '500+'

END

AS amount_level,

COUNT(*) AS orders,

ROUND(SUM(amount),2) AS GMV

FROM order_amount

GROUP BY amount_level;