-- Table: public.GAME_PUBLISHERS

-- DROP TABLE IF EXISTS public."GAME_PUBLISHERS";

CREATE TABLE IF NOT EXISTS public."GAME_PUBLISHERS"
(
    publisher_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_PUBLISHERS_pkey" PRIMARY KEY (publisher_id, game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_PUBLISHERS"
    OWNER to postgres;