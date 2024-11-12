-- Table: public.add_fund_record

-- DROP TABLE IF EXISTS public.add_fund_record;

CREATE TABLE IF NOT EXISTS public.add_fund_record
(
    add_fund_record_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    fund_change integer NOT NULL,
    "timestamp" time with time zone NOT NULL,
    CONSTRAINT add_fund_record_pkey PRIMARY KEY (add_fund_record_id),
    CONSTRAINT add_fund_record_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.add_fund_record
    OWNER to postgres;