SELECT bi.user_id, bi.game_id, SUM(bi.price) AS total_price
FROM public."buy_item" AS bi
WHERE bi."isCancelled" = false
GROUP BY bi.user_id, bi.game_id
ORDER BY bi.user_id, bi.game_id;