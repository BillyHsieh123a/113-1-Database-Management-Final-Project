-- Table: public.user

-- DROP TABLE IF EXISTS public."user";

CREATE TABLE IF NOT EXISTS public."user"
(
    user_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    password_hashed CHARACTER VARYING(20) COLLATE pg_catalog."default" NOT NULL,
    user_name CHARACTER VARYING(10) COLLATE pg_catalog."default" NOT NULL,
    user_description CHARACTER VARYING(300) COLLATE pg_catalog."default",
    profile_pic TEXT COLLATE pg_catalog."default",
    profile_background TEXT COLLATE pg_catalog."default",
    birthday DATE NOT NULL,
    email TEXT COLLATE pg_catalog."default" NOT NULL,
    country CHARACTER VARYING(20) COLLATE pg_catalog."default" NOT NULL,
    language CHARACTER VARYING(20) COLLATE pg_catalog."default" NOT NULL,
    fund INTEGER NOT NULL,
    filtering BOOLEAN NOT NULL,
    notification BOOLEAN NOT NULL,
    cookies BOOLEAN NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."user"
    OWNER TO postgres;
