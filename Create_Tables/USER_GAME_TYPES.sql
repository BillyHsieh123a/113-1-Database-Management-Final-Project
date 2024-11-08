-- Table: public.user_game_types

-- DROP TABLE IF EXISTS public.user_game_types;

CREATE TABLE IF NOT EXISTS public.user_game_types
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_type_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_game_types_pkey PRIMARY KEY (user_id, game_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_game_types
    OWNER to postgres;