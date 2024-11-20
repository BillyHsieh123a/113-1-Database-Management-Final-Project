-- Table: public.developers

-- DROP TABLE IF EXISTS public.developers;

CREATE TABLE IF NOT EXISTS public.developers
(
    developer_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    developer_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    description character varying(100) COLLATE pg_catalog."default",
    publisher_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "DEVELOPERS_pkey" PRIMARY KEY (developer_id),
    CONSTRAINT "DEVELOPERS_publisher_id_fkey" FOREIGN KEY (publisher_id)
        REFERENCES public.publishers (publisher_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.developers
    OWNER to postgres;