-- Table: public.user_game_statistics

-- DROP TABLE IF EXISTS public.user_game_statistics;

CREATE TABLE IF NOT EXISTS public.user_game_statistics
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    played_time interval,
    achievement_num integer,
    CONSTRAINT "USER_GAME_STATISTICS_pkey" PRIMARY KEY (user_id, game_id),
    CONSTRAINT "USER_GAME_STATISTICS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "USER_GAME_STATISTICS_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_game_statistics
    OWNER to postgres;