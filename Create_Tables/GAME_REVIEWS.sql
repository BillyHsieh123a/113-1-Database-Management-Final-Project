-- Table: public.game_reviews

-- DROP TABLE IF EXISTS public.game_reviews;

CREATE TABLE IF NOT EXISTS public.game_reviews
(
    review_timestamp timestamp with time zone,
    rating integer,
    review_id SERIAL NOT NULL,
    game_id SERIAL NOT NULL,
    user_id SERIAL NOT NULL,
    text character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "GAME_REVIEWS_pkey" PRIMARY KEY (review_id),
    CONSTRAINT "GAME_REVIEWS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "GAME_REVIEWS_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_reviews
    OWNER to postgres;