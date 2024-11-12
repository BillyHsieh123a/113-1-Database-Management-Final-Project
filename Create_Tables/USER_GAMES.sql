-- Table: public.user_games

-- DROP TABLE IF EXISTS public.user_games;

CREATE TABLE IF NOT EXISTS public.user_games
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    installed_date timestamp with time zone NOT NULL,
    uninstalled_date timestamp with time zone,
    CONSTRAINT "USER_GAMES_pkey" PRIMARY KEY (user_id, game_id, installed_date),
    CONSTRAINT "USER_GAMES_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "USER_GAMES_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_games
    OWNER to postgres;