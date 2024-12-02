-- Table: public.game

-- DROP TABLE IF EXISTS public.game;

CREATE TABLE IF NOT EXISTS public.game
(
    game_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    game_name CHARACTER VARYING(20) COLLATE pg_catalog."default",
    game_description CHARACTER VARYING(100) COLLATE pg_catalog."default",
    system_requirements CHARACTER VARYING(100) COLLATE pg_catalog."default",
    CONSTRAINT "GAME_pkey" PRIMARY KEY (game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game
    OWNER TO postgres;
