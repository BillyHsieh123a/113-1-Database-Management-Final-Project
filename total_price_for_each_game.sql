SELECT bi.game_id, SUM(bi.price) AS total_price
FROM public."buy_item" AS bi
WHERE bi."isCancelled" = false
GROUP BY bi.game_id;
