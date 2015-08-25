init:
    $ mods["lb__cardgame"] = u"Карточная игра и ничего больше"
    $ mod_tags["lb__cardgame"] = ["length:event","gameplay:minigame","character:Семён","character:Алиса","character:Лена","character:Ульяна","translation:russian"]

label lb__cardgame:
    $ VISIBLE = True
    menu:
        "Играть в закрытую":
            $ INVISIBLE = False
        "Играть в открытую":
            $ INVISIBLE = True
    menu:
        "Играть с Леной":
            $ rival = CardGameRivalUn(un_avatar_set,"Лена")
        "Играть с Ульяной":
            $ rival = CardGameRivalUs(us_avatar_set,"Ульяна")
        "Играть с Алисой":
            $ rival = CardGameRivalDv(dv_avatar_set,"Алиса")
    python:
        dialogs = {
                (0,"win","jump"):          "lb__cardgame_end",
                (0,"fail","jump"):         "lb__cardgame_end",
                (0,"draw","jump"):         "lb__cardgame_end",
            }
        generate_cards("bg hall",dialogs)
    jump cards_gameloop

label lb__cardgame_end:
    menu:
        "Играть ещё раз":
            jump lb__cardgame
        "Хватит играть":
            return
