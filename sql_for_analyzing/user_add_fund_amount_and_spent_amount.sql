CREATE INDEX user_bir ON public."user"(birthday);
DROP INDEX user_bir;

EXPLAIN SELECT bi.user_id, SUM(afr.fund_change) AS add_fund_amount, SUM(bi.price) AS spent_amount
FROM add_fund_record AS afr
JOIN buy_item AS bi ON bi.user_id = afr.user_id
JOIN public."user" ON public."user".user_id = bi.user_id
WHERE public."user".birthday > '2000-01-01'
GROUP BY bi.user_id
ORDER BY bi.user_id;