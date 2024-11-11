-- Table: public.ACHIEVEMENTS

-- DROP TABLE IF EXISTS public."ACHIEVEMENTS";

CREATE TABLE IF NOT EXISTS public."ACHIEVEMENTS"
(
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    achievement_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "ACHIEVEMENTS_pkey" PRIMARY KEY (game_id, achievement_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ACHIEVEMENTS"
    OWNER to postgres;