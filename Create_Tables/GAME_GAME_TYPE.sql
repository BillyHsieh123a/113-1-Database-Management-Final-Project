-- Table: public.GAME_GAME_TYPE

-- DROP TABLE IF EXISTS public."GAME_GAME_TYPE";

CREATE TABLE IF NOT EXISTS public."GAME_GAME_TYPE"
(
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_type_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_GAME_TYPE_pkey" PRIMARY KEY (game_id, game_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_GAME_TYPE"
    OWNER to postgres;