-- Table: public.PUBLISHERS

-- DROP TABLE IF EXISTS public."PUBLISHERS";

CREATE TABLE IF NOT EXISTS public."PUBLISHERS"
(
    publisher_id character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    publisher_name character varying(20)[] COLLATE pg_catalog."default",
    description character varying(100)[] COLLATE pg_catalog."default",
    CONSTRAINT "PUBLISHERS_pkey" PRIMARY KEY (publisher_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."PUBLISHERS"
    OWNER to postgres;