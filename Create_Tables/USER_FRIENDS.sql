-- Table: public.user_friends

-- DROP TABLE IF EXISTS public.user_friends;

CREATE TABLE IF NOT EXISTS public.user_friends
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    friend_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_friends_pkey PRIMARY KEY (user_id, friend_id),
    CONSTRAINT user_friends_friend_id_fkey FOREIGN KEY (friend_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_friends_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_friends
    OWNER to postgres;