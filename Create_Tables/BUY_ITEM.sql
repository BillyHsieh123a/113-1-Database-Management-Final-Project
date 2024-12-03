-- Table: public.buy_item

-- DROP TABLE IF EXISTS public.buy_item;

CREATE TABLE IF NOT EXISTS public.buy_item
(
    price INTEGER,
    "timestamp" TIMESTAMP WITH TIME ZONE,
    "isCancelled" BOOLEAN,
    buy_item_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    user_id SERIAL NOT NULL,
    game_id SERIAL NOT NULL,
    item_id CHARACTER VARYING(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "BUY_ITEM_pkey" PRIMARY KEY (buy_item_id, game_id, item_id),
    CONSTRAINT buy_item_game_id_item_id_fkey FOREIGN KEY (game_id, item_id)
        REFERENCES public.game_item (game_id, item_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT buy_item_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.buy_item
    OWNER TO postgres;
