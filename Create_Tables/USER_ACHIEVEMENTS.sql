-- Table: public.user_achievements

-- DROP TABLE IF EXISTS public.user_achievements;

CREATE TABLE IF NOT EXISTS public.user_achievements
(
    user_id SERIAL NOT NULL,
    game_id SERIAL NOT NULL,
    achievement_id SERIAL NOT NULL,
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