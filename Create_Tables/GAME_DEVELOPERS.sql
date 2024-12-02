-- Table: public.game_developers

-- DROP TABLE IF EXISTS public.game_developers;

CREATE TABLE IF NOT EXISTS public.game_developers
(
    game_developer_id SERIAL NOT NULL, -- Added an auto-incrementing ID
    developer_id CHARACTER VARYING(10) COLLATE pg_catalog."default" NOT NULL,
    game_id CHARACTER VARYING(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_DEVELOPERS_pkey" PRIMARY KEY (game_developer_id), -- Primary key on the new auto-incrementing ID
    CONSTRAINT "GAME_DEVELOPERS_developer_id_fkey" FOREIGN KEY (developer_id)
        REFERENCES public.developers (developer_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "GAME_DEVELOPERS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_developers
    OWNER TO postgres;
