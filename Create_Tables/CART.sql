-- Table: public.CART

-- DROP TABLE IF EXISTS public."CART";

CREATE TABLE IF NOT EXISTS public."CART"
(
    user_id character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "CART_pkey" PRIMARY KEY (user_id, game_id, item_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."CART"
    OWNER to postgres;