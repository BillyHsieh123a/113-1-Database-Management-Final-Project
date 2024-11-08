-- Table: public.user_devices

-- DROP TABLE IF EXISTS public.user_devices;

CREATE TABLE IF NOT EXISTS public.user_devices
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    device_id integer NOT NULL,
    device_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    type character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_devices_pkey PRIMARY KEY (user_id, device_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_devices
    OWNER to postgres;