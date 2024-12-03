-- Table: public.game_types

-- DROP TABLE IF EXISTS public.game_types;

CREATE TABLE IF NOT EXISTS public.game_types
(
    game_type_id SERIAL NOT NULL,
    game_type_name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT game_types_pkey PRIMARY KEY (game_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_types
    OWNER to postgres;