-- Table: public.GAME

-- DROP TABLE IF EXISTS public."GAME";

CREATE TABLE IF NOT EXISTS public."GAME"
(
    game_id character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    game_name character varying(20)[] COLLATE pg_catalog."default",
    game_description character varying(100)[] COLLATE pg_catalog."default",
    system_requiementsr character varying(100)[] COLLATE pg_catalog."default",
    CONSTRAINT "GAME_pkey" PRIMARY KEY (game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME"
    OWNER to postgres;