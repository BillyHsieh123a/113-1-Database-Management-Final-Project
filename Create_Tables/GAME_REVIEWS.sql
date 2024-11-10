-- Table: public.GAME_REVIEWS

-- DROP TABLE IF EXISTS public."GAME_REVIEWS";

CREATE TABLE IF NOT EXISTS public."GAME_REVIEWS"
(
    review_id character varying(100)[] COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10)[] COLLATE pg_catalog."default",
    user_id character varying(10)[] COLLATE pg_catalog."default",
    review_timestamp timestamp with time zone,
    rating integer,
    text character varying(100)[] COLLATE pg_catalog."default",
    CONSTRAINT "GAME_REVIEWS_pkey" PRIMARY KEY (review_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_REVIEWS"
    OWNER to postgres;