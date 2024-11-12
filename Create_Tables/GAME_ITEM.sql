-- Table: public.game_item

-- DROP TABLE IF EXISTS public.game_item;

CREATE TABLE IF NOT EXISTS public.game_item
(
    original_price integer,
    current_price integer,
    special_offer double precision,
    release_date date,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_ITEM_pkey" PRIMARY KEY (item_id, game_id),
    CONSTRAINT "GAME_ITEM_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_item
    OWNER to postgres;