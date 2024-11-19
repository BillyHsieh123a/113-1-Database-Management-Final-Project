-- Start of ACHIEVEMENTS.sql
-- Table: public.ACHIEVEMENTS

-- DROP TABLE IF EXISTS public."ACHIEVEMENTS";

CREATE TABLE IF NOT EXISTS public."ACHIEVEMENTS"
(
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    achievement_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "ACHIEVEMENTS_pkey" PRIMARY KEY (game_id, achievement_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ACHIEVEMENTS"
    OWNER to postgres;
-- End of ACHIEVEMENTS.sql

-- Start of ADD_FUND_RECORD.sql
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
-- End of ADD_FUND_RECORD.sql

-- Start of BUY_ITEM.sql
-- Table: public.buy_item

-- DROP TABLE IF EXISTS public.buy_item;

CREATE TABLE IF NOT EXISTS public.buy_item
(
    price integer,
    "timestamp" timestamp with time zone,
    "isCancelled" boolean,
    buy_item_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    user_id character varying(10) COLLATE pg_catalog."default",
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "BUY_ITEM_pkey" PRIMARY KEY (buy_item_id, game_id, item_id),
    CONSTRAINT buy_item_game_id_item_id_fkey FOREIGN KEY (game_id, item_id)
        REFERENCES public.game_item (game_id, item_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT buy_item_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.buy_item
    OWNER to postgres;
-- End of BUY_ITEM.sql

-- Start of BUY_ITEM_CANCELL.sql
-- Table: public.buy_item_cancel

-- DROP TABLE IF EXISTS public.buy_item_cancel;

CREATE TABLE IF NOT EXISTS public.buy_item_cancel
(
    buy_item_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone,
    CONSTRAINT buy_item_cancel_pkey PRIMARY KEY (buy_item_id, game_id, item_id),
    CONSTRAINT buy_item_cancel_buy_item_id_game_id_item_id_fkey FOREIGN KEY (buy_item_id, game_id, item_id)
        REFERENCES public.buy_item (buy_item_id, game_id, item_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.buy_item_cancel
    OWNER to postgres;
-- End of BUY_ITEM_CANCELL.sql

-- Start of CART.sql
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
-- End of CART.sql

-- Start of DEVELOPERS.sql
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
-- End of DEVELOPERS.sql

-- Start of GAME.sql
-- Table: public.GAME

-- DROP TABLE IF EXISTS public."GAME";

CREATE TABLE IF NOT EXISTS public."GAME"
(
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_name character varying(20) COLLATE pg_catalog."default",
    game_description character varying(100) COLLATE pg_catalog."default",
    system_reuirements character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "GAME_pkey" PRIMARY KEY (game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME"
    OWNER to postgres;
-- End of GAME.sql

-- Start of GAME_DEVELOPERS.sql
-- Table: public.game_developers

-- DROP TABLE IF EXISTS public.game_developers;

CREATE TABLE IF NOT EXISTS public.game_developers
(
    developer_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_DEVELOPERS_pkey" PRIMARY KEY (developer_id, game_id),
    CONSTRAINT "GAME_DEVELOPERS_developer_id_fkey" FOREIGN KEY (developer_id)
        REFERENCES public.developers (developer_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "GAME_DEVELOPERS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_developers
    OWNER to postgres;
-- End of GAME_DEVELOPERS.sql

-- Start of GAME_GAME_TYPE.sql
-- Table: public.game_game_type

-- DROP TABLE IF EXISTS public.game_game_type;

CREATE TABLE IF NOT EXISTS public.game_game_type
(
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_type_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_GAME_TYPE_pkey" PRIMARY KEY (game_id, game_type_id),
    CONSTRAINT game_game_type_game_id_fkey FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT game_game_type_game_type_id_fkey FOREIGN KEY (game_type_id)
        REFERENCES public.game_types (game_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_game_type
    OWNER to postgres;
-- End of GAME_GAME_TYPE.sql

-- Start of GAME_ITEM.sql
-- Table: public.game_item

-- DROP TABLE IF EXISTS public.game_item;

CREATE TABLE IF NOT EXISTS public.game_item
(
    original_price integer,
    current_price integer,
    special_offer double precision,
    release_date date,
    item_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_ITEM_pkey" PRIMARY KEY (item_id, game_id),
    CONSTRAINT "GAME_ITEM_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_item
    OWNER to postgres;
-- End of GAME_ITEM.sql

-- Start of GAME_PUBLISHERS.sql
-- Table: public.GAME_PUBLISHERS

-- DROP TABLE IF EXISTS public."GAME_PUBLISHERS";

CREATE TABLE IF NOT EXISTS public."GAME_PUBLISHERS"
(
    publisher_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "GAME_PUBLISHERS_pkey" PRIMARY KEY (publisher_id, game_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."GAME_PUBLISHERS"
    OWNER to postgres;
-- End of GAME_PUBLISHERS.sql

-- Start of GAME_REVIEWS.sql
-- Table: public.game_reviews

-- DROP TABLE IF EXISTS public.game_reviews;

CREATE TABLE IF NOT EXISTS public.game_reviews
(
    review_timestamp timestamp with time zone,
    rating integer,
    review_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default",
    user_id character varying(10) COLLATE pg_catalog."default",
    text character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "GAME_REVIEWS_pkey" PRIMARY KEY (review_id),
    CONSTRAINT "GAME_REVIEWS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "GAME_REVIEWS_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_reviews
    OWNER to postgres;
-- End of GAME_REVIEWS.sql

-- Start of GAME_TYPES.sql
-- Table: public.game_types

-- DROP TABLE IF EXISTS public.game_types;

CREATE TABLE IF NOT EXISTS public.game_types
(
    game_type_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_type_name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT game_types_pkey PRIMARY KEY (game_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_types
    OWNER to postgres;
-- End of GAME_TYPES.sql

-- Start of PUBLISHERS.sql
-- Table: public.publishers

-- DROP TABLE IF EXISTS public.publishers;

CREATE TABLE IF NOT EXISTS public.publishers
(
    publisher_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    publisher_name character varying(20) COLLATE pg_catalog."default",
    description character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT "PUBLISHERS_pkey" PRIMARY KEY (publisher_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.publishers
    OWNER to postgres;
-- End of PUBLISHERS.sql

-- Start of USER.sql
-- Table: public.user

-- DROP TABLE IF EXISTS public."user";

CREATE TABLE IF NOT EXISTS public."user"
(
    user_id character(10) COLLATE pg_catalog."default" NOT NULL,
    password_hashed character varying(20) COLLATE pg_catalog."default" NOT NULL,
    user_name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    user_description character varying(300) COLLATE pg_catalog."default",
    profile_pic text COLLATE pg_catalog."default",
    profile_background text COLLATE pg_catalog."default",
    birthday date NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    country character varying(20) COLLATE pg_catalog."default" NOT NULL,
    language character varying(20) COLLATE pg_catalog."default" NOT NULL,
    fund integer NOT NULL,
    filtering boolean NOT NULL,
    notification boolean NOT NULL,
    cookies boolean NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."user"
    OWNER to postgres;
-- End of USER.sql

-- Start of USER_ACHIEVEMENTS.sql
-- Table: public.user_achievements

-- DROP TABLE IF EXISTS public.user_achievements;

CREATE TABLE IF NOT EXISTS public.user_achievements
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    achievement_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    achieved_date timestamp with time zone,
    CONSTRAINT "USER_ACHIEVEMENTS_pkey" PRIMARY KEY (user_id, achievement_id),
    CONSTRAINT "USER_ACHIEVEMENTS_achievement_id_game_id_fkey" FOREIGN KEY (achievement_id, game_id)
        REFERENCES public.achievements (achievement_id, game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "USER_ACHIEVEMENTS_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_achievements
    OWNER to postgres;
-- End of USER_ACHIEVEMENTS.sql

-- Start of USER_DEVICES.sql
-- Table: public.user_devices

-- DROP TABLE IF EXISTS public.user_devices;

CREATE TABLE IF NOT EXISTS public.user_devices
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    device_id integer NOT NULL,
    device_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    type character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_devices_pkey PRIMARY KEY (user_id, device_id),
    CONSTRAINT user_devices_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_devices
    OWNER to postgres;
-- End of USER_DEVICES.sql

-- Start of USER_FRIENDS.sql
-- Table: public.user_friends

-- DROP TABLE IF EXISTS public.user_friends;

CREATE TABLE IF NOT EXISTS public.user_friends
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    friend_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_friends_pkey PRIMARY KEY (user_id, friend_id),
    CONSTRAINT user_friends_friend_id_fkey FOREIGN KEY (friend_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_friends_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_friends
    OWNER to postgres;
-- End of USER_FRIENDS.sql

-- Start of USER_GAMES.sql
-- Table: public.user_games

-- DROP TABLE IF EXISTS public.user_games;

CREATE TABLE IF NOT EXISTS public.user_games
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    installed_date timestamp with time zone NOT NULL,
    uninstalled_date timestamp with time zone,
    CONSTRAINT "USER_GAMES_pkey" PRIMARY KEY (user_id, game_id, installed_date),
    CONSTRAINT "USER_GAMES_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "USER_GAMES_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_games
    OWNER to postgres;
-- End of USER_GAMES.sql

-- Start of USER_GAME_STATISTICS.sql
-- Table: public.user_game_statistics

-- DROP TABLE IF EXISTS public.user_game_statistics;

CREATE TABLE IF NOT EXISTS public.user_game_statistics
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    played_time interval,
    achievement_num integer,
    CONSTRAINT "USER_GAME_STATISTICS_pkey" PRIMARY KEY (user_id, game_id),
    CONSTRAINT "USER_GAME_STATISTICS_game_id_fkey" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "USER_GAME_STATISTICS_user_id_fkey" FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_game_statistics
    OWNER to postgres;
-- End of USER_GAME_STATISTICS.sql

-- Start of USER_GAME_TYPES.sql
-- Table: public.user_game_types

-- DROP TABLE IF EXISTS public.user_game_types;

CREATE TABLE IF NOT EXISTS public.user_game_types
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_type_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_game_types_pkey PRIMARY KEY (user_id, game_type_id),
    CONSTRAINT user_game_types_game_type_id_fkey FOREIGN KEY (game_type_id)
        REFERENCES public.game_types (game_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_game_types_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_game_types
    OWNER to postgres;
-- End of USER_GAME_TYPES.sql

-- Start of USER_INVENTORY.sql
-- Table: public.user_inventory

-- DROP TABLE IF EXISTS public.user_inventory;

CREATE TABLE IF NOT EXISTS public.user_inventory
(
    user_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
    game_id character varying(10) COLLATE pg_catalog."default" NOT NULL,
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
-- End of USER_INVENTORY.sql

