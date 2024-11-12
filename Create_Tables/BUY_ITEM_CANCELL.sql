-- Table: public.buy_item_cancel

-- DROP TABLE IF EXISTS public.buy_item_cancel;

CREATE TABLE IF NOT EXISTS public.buy_item_cancel
(
    buy_item_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone,
    CONSTRAINT buy_item_cancel_pkey PRIMARY KEY (buy_item_id, game_id, item_id),
    CONSTRAINT buy_item_cancel_buy_item_id_game_id_item_id_fkey FOREIGN KEY (buy_item_id, game_id, item_id)
        REFERENCES public.buy_item (buy_item_id, game_id, item_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.buy_item_cancel
    OWNER to postgres;