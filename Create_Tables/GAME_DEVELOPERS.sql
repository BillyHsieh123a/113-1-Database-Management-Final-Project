-- Table: public.GAME_DEVELOPERS

-- DROP TABLE IF EXISTS public."GAME_DEVELOPERS";

CREATE TABLE IF NOT EXISTS public."GAME_DEVELOPERS"
(
    developer_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_DEVELOPERS_pkey" PRIMARY KEY (developer_id, game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_DEVELOPERS"
    OWNER to postgres;