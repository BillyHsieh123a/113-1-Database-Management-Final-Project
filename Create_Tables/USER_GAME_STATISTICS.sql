-- Table: public.USER_GAME_STATISTICS

-- DROP TABLE IF EXISTS public."USER_GAME_STATISTICS";

CREATE TABLE IF NOT EXISTS public."USER_GAME_STATISTICS"
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    played_time interval,
    achievement_num integer,
    CONSTRAINT "USER_GAME_STATISTICS_pkey" PRIMARY KEY (user_id, game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."USER_GAME_STATISTICS"
    OWNER to postgres;