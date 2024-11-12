-- Table: public.user_devices

-- DROP TABLE IF EXISTS public.user_devices;

CREATE TABLE IF NOT EXISTS public.user_devices
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    device_id integer NOT NULL,
    device_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    type character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_devices_pkey PRIMARY KEY (user_id, device_id),
    CONSTRAINT user_devices_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_devices
    OWNER to postgres;