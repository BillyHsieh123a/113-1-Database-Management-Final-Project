-- Table: public.publishers

-- DROP TABLE IF EXISTS public.publishers;

CREATE TABLE IF NOT EXISTS public.publishers
(
    publisher_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    publisher_name CHARACTER VARYING(20) COLLATE pg_catalog."default",
    description CHARACTER VARYING(100) COLLATE pg_catalog."default",
    CONSTRAINT "PUBLISHERS_pkey" PRIMARY KEY (publisher_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.publishers
    OWNER TO postgres;
