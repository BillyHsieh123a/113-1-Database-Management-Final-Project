-- Table: public.buy_item

-- DROP TABLE IF EXISTS public.buy_item;

CREATE TABLE IF NOT EXISTS public.buy_item
(
    price integer,
    "timestamp" timestamp with time zone,
    "isCancelled" boolean,
    buy_item_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    user_id character varying(10) COLLATE pg_catalog."default",
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
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
    OWNER to postgres;