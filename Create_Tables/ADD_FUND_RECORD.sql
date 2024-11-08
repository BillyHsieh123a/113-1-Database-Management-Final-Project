-- Table: public.add_fund_record

-- DROP TABLE IF EXISTS public.add_fund_record;

CREATE TABLE IF NOT EXISTS public.add_fund_record
(
    add_fund_record_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    fund_change integer NOT NULL,
    "timestamp" time with time zone NOT NULL,
    CONSTRAINT add_fund_record_pkey PRIMARY KEY (add_fund_record_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.add_fund_record
    OWNER to postgres;