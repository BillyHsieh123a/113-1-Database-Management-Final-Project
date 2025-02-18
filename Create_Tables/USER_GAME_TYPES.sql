-- Table: public.user_game_types

-- DROP TABLE IF EXISTS public.user_game_types;

CREATE TABLE IF NOT EXISTS public.user_game_types
(
    user_id SERIAL NOT NULL,
    game_type_id SERIAL NOT NULL,
    CONSTRAINT user_game_types_pkey PRIMARY KEY (user_id, game_type_id),
    CONSTRAINT user_game_types_game_type_id_fkey FOREIGN KEY (game_type_id)
        REFERENCES public.game_types (game_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_game_types_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_game_types
    OWNER to postgres;