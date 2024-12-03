-- Table: public.user_inventory

-- DROP TABLE IF EXISTS public.user_inventory;

CREATE TABLE IF NOT EXISTS public.user_inventory
(
    user_id SERIAL NOT NULL,
    game_id SERIAL NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    acquired_date timestamp with time zone NOT NULL,
    not_owned_date timestamp with time zone,
    CONSTRAINT "USER_INVENTORY_pkey" PRIMARY KEY (user_id, item_id, acquired_date),
    CONSTRAINT "USER_INVENTORY_game_id_item_id_fkey" FOREIGN KEY (game_id, item_id)
        REFERENCES public.game_item (game_id, item_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "USER_INVENTORY_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_inventory
    OWNER to postgres;