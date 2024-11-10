-- Table: public.GAME_ITEM

-- DROP TABLE IF EXISTS public."GAME_ITEM";

CREATE TABLE IF NOT EXISTS public."GAME_ITEM"
(
    original_price integer,
    current_price integer,
    special_offer double precision,
    release_date date,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_ITEM_pkey" PRIMARY KEY (item_id, game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_ITEM"
    OWNER to postgres;