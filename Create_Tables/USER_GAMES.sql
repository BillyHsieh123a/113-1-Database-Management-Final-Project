-- Table: public.USER_GAMES

-- DROP TABLE IF EXISTS public."USER_GAMES";

CREATE TABLE IF NOT EXISTS public."USER_GAMES"
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    installed_date timestamp with time zone NOT NULL,
    uninstalled_date timestamp with time zone,
    CONSTRAINT "USER_GAMES_pkey" PRIMARY KEY (user_id, game_id, installed_date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."USER_GAMES"
    OWNER to postgres;