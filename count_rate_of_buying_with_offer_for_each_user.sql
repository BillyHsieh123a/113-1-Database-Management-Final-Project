SELECT bi.user_id, COUNT(CASE WHEN bi.price < gi.original_price THEN 1 END) * 1.0 / COUNT(*) AS buying_with_offer_rate
FROM public."buy_item" AS bi
JOIN public."game_item" AS gi ON bi.game_id = gi.game_id AND bi.item_id = gi.item_id
WHERE bi."isCancelled" = false
GROUP BY bi.user_id
ORDER BY bi.user_id;
