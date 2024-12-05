-- cost:218.75
CREATE INDEX game_publishers_game_id ON public."game_publishers"("game_id");
DROP INDEX game_publishers_game_id

-- did not use this
CREATE INDEX buy_item_game_id ON public."buy_item"("game_id");
DROP INDEX buy_item_game_id

-- cost 249.89
EXPLAIN SELECT gp.publisher_id, SUM(bi.price) AS total_price
FROM public."buy_item" AS bi
JOIN public."game_publishers" AS gp ON bi.game_id = gp.game_id
WHERE bi."isCancelled" = false
GROUP BY gp.publisher_id
ORDER BY gp.publisher_id;