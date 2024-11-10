-- Table: public.GAME_ITEM

-- DROP TABLE IF EXISTS public."GAME_ITEM";

CREATE TABLE IF NOT EXISTS public."GAME_ITEM"
(
    item_id character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10)[] COLLATE pg_catalog."default",
    original_price integer,
    current_price integer,
    special_offer double precision,
    release_date date,
    CONSTRAINT "GAME_ITEM_pkey" PRIMARY KEY (item_id),
    CONSTRAINT "GAME_ITEM_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public."GAME" (game_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_ITEM"
    OWNER to postgres;