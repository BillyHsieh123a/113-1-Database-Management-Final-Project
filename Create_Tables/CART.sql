-- Table: public.CART

-- DROP TABLE IF EXISTS public."CART";

CREATE TABLE IF NOT EXISTS public."CART"
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "CART_pkey" PRIMARY KEY (user_id, game_id, item_id),
    CONSTRAINT "CART_game_id_item_id_fkey" FOREIGN KEY (game_id, item_id)
        REFERENCES public."GAME_ITEM" (game_id, item_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "CART_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."CART"
    OWNER to postgres;