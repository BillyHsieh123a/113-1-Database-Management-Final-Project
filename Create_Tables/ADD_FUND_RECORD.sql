-- Table: public.add_fund_record

-- DROP TABLE IF EXISTS public.add_fund_record;

CREATE TABLE IF NOT EXISTS public.add_fund_record
(
    add_fund_record_id SERIAL NOT NULL, -- Changed to SERIAL for auto-increment
    user_id SERIAL NOT NULL,
    fund_change INTEGER NOT NULL,
    "timestamp" TIME WITH TIME ZONE NOT NULL,
    CONSTRAINT add_fund_record_pkey PRIMARY KEY (add_fund_record_id),
    CONSTRAINT add_fund_record_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.add_fund_record
    OWNER TO postgres;
