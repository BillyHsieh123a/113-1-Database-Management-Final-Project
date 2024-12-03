-- Table: public.game_game_type

-- DROP TABLE IF EXISTS public.game_game_type;

CREATE TABLE IF NOT EXISTS public.game_game_type
(
    game_id SERIAL NOT NULL,
    game_type_id SERIAL NOT NULL,
    CONSTRAINT "GAME_GAME_TYPE_pkey" PRIMARY KEY (game_id, game_type_id),
    CONSTRAINT game_game_type_game_id_fkey FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT game_game_type_game_type_id_fkey FOREIGN KEY (game_type_id)
        REFERENCES public.game_types (game_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_game_type
    OWNER to postgres;