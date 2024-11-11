-- Table: public.USER_INVENTORY

-- DROP TABLE IF EXISTS public."USER_INVENTORY";

CREATE TABLE IF NOT EXISTS public."USER_INVENTORY"
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    acquired_date timestamp with time zone NOT NULL,
    not_owned_date timestamp with time zone,
    CONSTRAINT "USER_INVENTORY_pkey" PRIMARY KEY (user_id, item_id, acquired_date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."USER_INVENTORY"
    OWNER to postgres;