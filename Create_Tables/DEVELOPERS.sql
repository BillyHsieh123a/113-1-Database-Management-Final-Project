-- Table: public.developers

-- DROP TABLE IF EXISTS public.developers;

CREATE TABLE IF NOT EXISTS public.developers
(
    developer_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    developer_name CHARACTER VARYING(20) COLLATE pg_catalog."default" NOT NULL,
    description CHARACTER VARYING(100) COLLATE pg_catalog."default",
    publisher_id SERIAL NOT NULL,
    CONSTRAINT "DEVELOPERS_pkey" PRIMARY KEY (developer_id),
    CONSTRAINT "DEVELOPERS_publisher_id_fkey" FOREIGN KEY (publisher_id)
        REFERENCES public.publishers (publisher_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.developers
    OWNER TO postgres;
