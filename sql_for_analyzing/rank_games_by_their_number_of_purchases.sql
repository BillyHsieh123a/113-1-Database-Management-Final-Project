CREATE INDEX but_item_item_id 
ON buy_item(item_id)

DROP INDEX but_item_item_id
-- before creating index: cost: 19.34
-- after creating index: cost: 12.70
EXPLAIN SELECT bi.game_id, COUNT(*) AS game_purchase_count
FROM public."buy_item" AS bi
WHERE bi."isCancelled" = false AND bi.item_id = '1'
GROUP BY bi.game_id
ORDER BY game_purchase_count DESC
LIMIT 10;

