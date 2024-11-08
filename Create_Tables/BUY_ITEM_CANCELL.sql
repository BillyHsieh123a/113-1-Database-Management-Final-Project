-- Table: public.buy_item_cancel

-- DROP TABLE IF EXISTS public.buy_item_cancel;

CREATE TABLE IF NOT EXISTS public.buy_item_cancel
(
    buy_item_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone,
    CONSTRAINT buy_item_cancel_pkey PRIMARY KEY (buy_item_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.buy_item_cancel
    OWNER to postgres;