-- Table: public.publishers

-- DROP TABLE IF EXISTS public.publishers;

CREATE TABLE IF NOT EXISTS public.publishers
(
    publisher_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    publisher_name character varying(20) COLLATE pg_catalog."default",
    description character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "PUBLISHERS_pkey" PRIMARY KEY (publisher_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.publishers
    OWNER to postgres;