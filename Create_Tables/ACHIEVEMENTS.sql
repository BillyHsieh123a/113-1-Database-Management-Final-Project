-- Table: public.achievements

-- DROP TABLE IF EXISTS public.achievements;

CREATE TABLE IF NOT EXISTS public.achievements
(
    game_id SERIAL NOT NULL,
    achievement_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    achievement_name CHARACTER VARYING(10) COLLATE pg_catalog."default" NOT NULL,
    achievement_description CHARACTER VARYING(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "ACHIEVEMENTS_pkey" PRIMARY KEY (game_id, achievement_id),
    CONSTRAINT "ACHIEVEMENTS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.achievements
    OWNER to postgres;
