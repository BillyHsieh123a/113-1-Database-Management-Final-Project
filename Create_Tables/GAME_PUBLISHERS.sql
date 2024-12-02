-- Table: public.game_publishers

-- DROP TABLE IF EXISTS public.game_publishers;

CREATE TABLE IF NOT EXISTS public.game_publishers
(
    game_publisher_id SERIAL NOT NULL, -- Added an auto-incrementing ID
    publisher_id SERIAL NOT NULL,
    game_id SERIAL NOT NULL,
    CONSTRAINT "GAME_publishers_pkey" PRIMARY KEY (game_publisher_id), -- Primary key on the new auto-incrementing ID
    CONSTRAINT "GAME_publishers_publisher_id_fkey" FOREIGN KEY (publisher_id)
        REFERENCES public.publishers (publisher_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "GAME_publishers_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_publishers
    OWNER TO postgres;
