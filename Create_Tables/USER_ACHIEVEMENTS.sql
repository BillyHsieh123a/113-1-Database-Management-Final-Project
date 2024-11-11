-- Table: public.USER_ACHIEVEMENTS

-- DROP TABLE IF EXISTS public."USER_ACHIEVEMENTS";

CREATE TABLE IF NOT EXISTS public."USER_ACHIEVEMENTS"
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    achievement_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    achieved_date timestamp with time zone,
    CONSTRAINT "USER_ACHIEVEMENTS_pkey" PRIMARY KEY (user_id, achievement_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."USER_ACHIEVEMENTS"
    OWNER to postgres;