-- Table: public.DEVELOPERS

-- DROP TABLE IF EXISTS public."DEVELOPERS";

CREATE TABLE IF NOT EXISTS public."DEVELOPERS"
(
    developer_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    developer_name character varying(20) COLLATE pg_catalog."default",
    description character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "DEVELOPERS_pkey" PRIMARY KEY (developer_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."DEVELOPERS"
    OWNER to postgres;