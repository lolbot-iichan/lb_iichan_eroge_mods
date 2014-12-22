init:
    $ mods["lb__guitar_start"] = u"Алиса учит Семёна играть на гитаре"
    $ mod_tags["lb__guitar_start"] = ["length:event","gameplay:minigame","protagonist:male","character:Семён","character:Алиса","translation:english","translation:russian"]

translate english strings:
    old "Алиса учит Семёна играть на гитаре"
    new "Alisa teachs Semyon to play guitar"

init python:
    guitar_scene = "mods/lb_guitar/guitar1920.png"
    guitar_b = "mods/lb_guitar/index_fingerprint.png"
    guitar_g = "mods/lb_guitar/index_fingerprint_green.png"
    guitar_r = "mods/lb_guitar/index_fingerprint_red.png"

    guitar_buttons_some = {
        "H-": [188, 515, "sound/sfx/guitar/h.ogg"],
        "D-": [404, 515, "sound/sfx/guitar/d.ogg"],
        "E-": [530, 515, "sound/sfx/guitar/e.ogg"],
        "F-": [589, 515, "sound/sfx/guitar/f.ogg"]
    }
    guitar_buttons_all = guitar_buttons_some.copy()
    guitar_buttons_all.update({
        "C-": [264, 515, "sound/sfx/guitar/c.ogg"],
        "C#": [337, 515, "sound/sfx/guitar/c#.ogg"],
        "D#": [470, 515, "sound/sfx/guitar/d#.ogg"],
        "F#": [643, 515, "sound/sfx/guitar/f#.ogg"]
    })
    
    guitar_demopause = 0.25
    
    def create_guitar_list(buttons):
        guitar_piclist = [(1920,1080),(0,0),guitar_scene]
        for i,j in buttons.iteritems():
            guitar_piclist += [(j[0],j[1]),guitar_b]
        return guitar_piclist

    renpy.image("guitar scene",guitar_scene)
    renpy.image("guitar all",im.Composite(*create_guitar_list(guitar_buttons_all)))
    renpy.image("guitar some",im.Composite(*create_guitar_list(guitar_buttons_some)))

    def guitar_bg(buttons):
        renpy.scene()
        renpy.show("bg black")
        if  buttons == None:
            renpy.show("guitar scene")
        elif buttons == guitar_buttons_some:
            renpy.show("guitar some")
        else:
            renpy.show("guitar all")

    def guitar_demoplay(melody,buttons):
        for i in melody:
            guitar_bg(buttons)
            for k,x in buttons.iteritems():
                if k == i[:2]:
                    ui.image(guitar_r,xpos=x[0],ypos=x[1])
            if i[:2] in buttons:
                renpy.sound.play(buttons[i[:2]][2])
            else:
                renpy.sound.stop()
            if i[3:]:
                renpy.pause(guitar_demopause*int(i[3:]))
            else:
                renpy.pause(guitar_demopause)
        renpy.pause(1.0)

    def guitar_waitplay(melody,buttons):
        for i in melody:
            guitar_bg(None)
            for k,x in buttons.iteritems():
                if x[2]:
                    ui.imagebutton(guitar_b,guitar_g,clicked=ui.returns(k),xpos=x[0],ypos=x[1])
            answer = ui.interact()
            renpy.sound.play(buttons[answer][2])
            if  answer != i:
                guitar_bg(buttons)
                return False
        guitar_bg(buttons)
        return True

label lb__guitar_start:
    $ guitar_fail = 0

    scene black
    $ guitar_bg(guitar_buttons_all)
    if  _preferences.language == "english":
        dv "Hi, Semyon. The whole city was covered by smoke recently, and now it's raining."    
        dv "I want you to learn how to play \"Smoke on the water\"."
        dv "For the beginning, play {i}si{/i} note, it's on the second fret."
    else:
        dv "Привет, Семен. Весь город недавно был в дыму, а теперь еще и дожди пошли."    
        dv "Я хочу научить тебя играть \"Smoke on the water\"."
        dv "Для начала, сыграй ноту {i}si{/i}, она на втором ладу."

label lb__guitar_si:
    $ guitar_demoplay(["H-"],guitar_buttons_all)
    if  guitar_waitplay(["H-"],guitar_buttons_all):
        if  _preferences.language == "english":
            dv "Yeah."
        else:
            dv "Угу."
    else:
        $ guitar_fail += 1
        if  guitar_fail < 3:
            if  _preferences.language == "english":
                dv "Well, no, look again..."
            else:
                dv "Да нет же, смотри..."
            jump lb__guitar_si
        jump lb__guitar_totalfail

    if  _preferences.language == "english":
        dv "The whole melody contains only 4 notes, you won't need the others."
        menu:
            "EASY MODE: Hide unused notes":
                $ guitar_buttons = guitar_buttons_some
            "MEDIUM MODE: Leave unused notes":
                $ guitar_buttons = guitar_buttons_all            
    else:
        dv "Вся мелодия играется на 4 нотах, остальные тебе не понадобятся."
        menu:
            "EASY MODE: Скрыть лишние ноты":
                $ guitar_buttons = guitar_buttons_some
            "MEDIUM MODE: Оставить лишние ноты":
                $ guitar_buttons = guitar_buttons_all            
    $ guitar_bg(guitar_buttons)

    if  _preferences.language == "english":
        dv "Try to play 3 notes in a row: {i}si-re-mi{/i}."
    else:
        dv "Попробуй сыграть 3 ноты подряд: {i}si-re-mi{/i}."

label lb__guitar_siremi: 
    $ guitar_demoplay(["H-/2","D-/2","E-/3"],guitar_buttons)
    if  guitar_waitplay(["H-","D-","E-"],guitar_buttons):
        if  _preferences.language == "english":
            dv "Correct."
        else:
            dv "Правильно."
    else:
        $ guitar_fail += 1
        if  guitar_fail < 3:
            if  _preferences.language == "english":
                dv "No, it's wrong, crap..."
            else:
                dv "Да ну нет же, блин..."
            jump lb__guitar_siremi
        jump lb__guitar_totalfail

    if  _preferences.language == "english":
        dv "Now repeat it, them play a similar block, but with note {i}fa{/i} almost at the very end."
    else:
        dv "Теперь играем тоже самое, затем почти такой же блок, только ноту {i}fa{/i} вставляем почти в самом конце."

label lb__guitar_siremisirefami:
    $ guitar_demoplay(["H-/2","D-/2","E-/3","H-/2","D-/2","F-/1","E-/4"],guitar_buttons)
    if  guitar_waitplay(["H-","D-","E-", "H-","D-","F-","E-"],guitar_buttons):
        if  _preferences.language == "english":
            dv "Yes!!!"
        else:
            dv "Да!!!"
    else:
        $ guitar_fail += 1
        if  guitar_fail < 3:
            if  _preferences.language == "english":
                dv "No. Try again."
            else:
                dv "Нет. Попробуй еще раз."
            jump lb__guitar_siremisirefami
        jump lb__guitar_totalfail

    if  _preferences.language == "english":
        dv "And now, everything together!!!"
        dv "{i}si-re-mi, si-re-fa-mi, si-re-mi, re-si{/i}"
    else:
        dv "А теперь, все вместе!!!"
        dv "{i}si-re-mi, si-re-fa-mi, si-re-mi, re-si{/i}"

label lb__guitar_final:
    $ guitar_demoplay(["H-/2","D-/2","E-/3", "H-/2","D-/2","F-/1","E-/4", "H-/2", "D-/2", "E-/3", "D-/2", "H-/3"],guitar_buttons)
    if  guitar_waitplay(["H-","D-","E-", "H-","D-","F-","E-", "H-", "D-", "E-", "D-", "H-"],guitar_buttons):
        scene cg epilogue_dv_3 with dissolve
        if  _preferences.language == "english":
            dv "You did it!{w} I'm so proud of you. You are cool enough for me to start dating you."
        else:
            dv "Получилось!{w} Я горжусь тобой. Ты такой офигенный, что я пожалуй буду с тобой встречаться."
        ".: GOOD END :."
        return
    else:
        $ guitar_fail += 1
        if  guitar_fail < 3:
            if  _preferences.language == "english":
                dv "It's wrong."
            else:
                dv "Не получилось."
            jump lb__guitar_final
        jump lb__guitar_totalfail

label lb__guitar_totalfail: 
        scene cg d5_dv_argue with dissolve
        if  _preferences.language == "english":
            dv "Semyon, you're a jerk!{w} I thought you are a real Man, but you would never become a metall band leader!!!{w} Go away, I don't want to see you!"
        else:
            dv "Семен, ты бестолочь!{w} Я думала, ты мужик, но из тебя никогда не получится лидера металл-группы!!!{w} Прочь, видеть тебя не хочу!"
        ".: BAD END :."
        return
