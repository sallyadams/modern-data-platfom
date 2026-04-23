SELECT
    user_id,
    SUM(amount) AS total_spent,
    COUNT(*) AS total_transactions
FROM {{ ref('stg_transactions') }}
GROUP BY user_id
