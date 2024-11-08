-- Table: public.user

-- DROP TABLE IF EXISTS public."user";

CREATE TABLE IF NOT EXISTS public."user"
(
    user_id character(10) COLLATE pg_catalog."default" NOT NULL,
    password_hashed character varying(20) COLLATE pg_catalog."default" NOT NULL,
    user_name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    user_description character varying(300) COLLATE pg_catalog."default",
    profile_pic text COLLATE pg_catalog."default",
    profile_background text COLLATE pg_catalog."default",
    birthday date NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    country character varying(20) COLLATE pg_catalog."default" NOT NULL,
    language character varying(20) COLLATE pg_catalog."default" NOT NULL,
    fund integer NOT NULL,
    filtering boolean NOT NULL,
    notification boolean NOT NULL,
    cookies boolean NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."user"
    OWNER to postgres;