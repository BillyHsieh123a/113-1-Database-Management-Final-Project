-- Table: public.BUY_ITEM

-- DROP TABLE IF EXISTS public."BUY_ITEM";

CREATE TABLE IF NOT EXISTS public."BUY_ITEM"
(
    price integer,
    "timestamp" timestamp with time zone,
    "isCancelled" boolean,
    buy_item_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    user_id character varying(10) COLLATE pg_catalog."default",
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "BUY_ITEM_pkey" PRIMARY KEY (buy_item_id, game_id, item_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."BUY_ITEM"
    OWNER to postgres;