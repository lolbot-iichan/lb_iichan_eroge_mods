init:
    $ mods["lb__miniedit_start"] = u"Мини-редактор"
    $ mod_tags["lb__miniedit_start"] = ["length:unlimited","gameplay:other","protagonist:male","character:Семён","character:Алиса","character:Славя","character:Женя","character:Шурик","character:Электроник","character:Ольга Дмитриевна","character:Виола","character:Лена","character:Мику","character:Юля","character:Пионер","character:Ульяна","translation:english","translation:russian"]

    $ lb__miniedit_allow_body = False
    $ lb__miniedit_allow_full = False

translate english strings:
    old "Мини-редактор"
    new "Mini-editor"
    old "Удалить текущий слот?!"
    new "Delete current slot?!"
    old "{b}КЛОНИРОВАТЬ{/b}"
    new "{b}CLONE{/b}"
    old "{b}УДАЛИТЬ{/b}"
    new "{b}DELETE{/b}"
    old "{b}ЗАПУСТИТЬ{/b}"
    new "{b}RUN{/b}"
    old "{b}КОПИРОВАТЬ КОД{/b}"
    new "{b}COPY SOURCE{/b}"
    old "{b}ЭКСПОРТИРОВАТЬ{/b}"
    new "{b}EXPORT{/b}"
    old "{b}ЭКСПОРТИРОВАТЬ В СВОЁМ ФОРМАТЕ{/b}"
    new "{b}EXPORT TO CUSTOM FORMAT{/b}"


label lb__miniedit_start:
    python:
        if  persistent.lb__miniedit_slots is None:
            persistent.lb__miniedit_slots = [
                    {
                        "time": "day",
                        "spritetime": "day",
                        "scene": "ext_path2_day",
                        "who": "me",
                        "what": "La-la-la, zhu-zhu-zhu, watashi wa la courbe de Lissajous.",
                        "show": [
                            {"who":"pi","emo":"normal","dress":"","close":"far","at":"cleft"},
                            {"who":"dv","emo":"rage","dress":"pioneer","close":"far","at":"cleft"},
                            {"who":"cs","emo":"smile","dress":"stethoscope","close":"far","at":"cright"},
                            {"who":"mt","emo":"rage","dress":"panama dress","close":"far","at":"left"},
                            {"who":"sl","emo":"tender","dress":"pioneer","close":"","at":"right"},
                            {"who":"el","emo":"scared","dress":"pioneer","close":"","at":"center"},
                            {"who":"mz","emo":"bukal","dress":"pioneer","close":"","at":"fright"},
                            {"who":"uv","emo":"laugh","dress":"","close":"","at":"left"},
                            {"who":"sh","emo":"cry","dress":"pioneer","close":"close","at":"fright"},
                            {"who":"un","emo":"surprise","dress":"pioneer","close":"close","at":"fleft"},
                            {"who":"mi","emo":"rage","dress":"swim","close":"close","at":"center"},
                            {"who":"us","emo":"shy","dress":"sport","close":"close","at":"right"},
                        ],
                    },
                    {
                        "time": "prolog",
                        "spritetime": "night",
                        "scene": "bus_stop",
                        "who": "uv",
                        "what": u"На улице - хня. Согрей меня, ня!",
                        "show": [ 
                            {"who":"uv","emo":"normal","dress":"","close":"close","at":"left"},
                        ],
                    },
                    {
                        "time": "sunset",
                        "spritetime": "sunset",
                        "scene": "ext_beach_sunset",
                        "who": "narrator",
                        "what": "Толпа малолеток преследовала меня.",
                        "show": [
                            {"who":"us","emo":"fear","dress":"pioneer","close":"far","at":"fright"},
                            {"who":"us","emo":"cry2","dress":"pioneer","close":"far","at":"fleft"},
                            {"who":"us","emo":"upset","dress":"pioneer","close":"far","at":"center"},
                            {"who":"us","emo":"shy","dress":"pioneer","close":"far","at":"cleft"},
                            {"who":"us","emo":"grin","dress":"pioneer","close":"far","at":"cright"},
                            {"who":"us","emo":"grin","dress":"pioneer","close":"","at":"right"},
                            {"who":"us","emo":"normal","dress":"pioneer","close":"","at":"cright"},
                            {"who":"us","emo":"sad","dress":"pioneer","close":"","at":"left"},
                            {"who":"us","emo":"surp3","dress":"pioneer","close":"close","at":"cleft"},
                            {"who":"us","emo":"sad","dress":"pioneer","close":"close","at":"cright"},
                            {"who":"us","emo":"smile","dress":"pioneer","close":"close","at":"center"},
                            {"who":"us","emo":"laugh","dress":"pioneer","close":"close","at":"right"},
                            {"who":"us","emo":"dontlike","dress":"pioneer","close":"close","at":"left"},
                        ],
                    },
                ]
        if  persistent.lb__miniedit_slot is None or persistent.lb__miniedit_slot not in range(len(persistent.lb__miniedit_slots)):
            persistent.lb__miniedit_slot = 0

        def lb__miniedit_get(p):
            return persistent.lb__miniedit_slots[persistent.lb__miniedit_slot][p]
        def lb__miniedit_set(p,v):
            persistent.lb__miniedit_slots[persistent.lb__miniedit_slot][p] = v

        def lb__miniedit_upd_time():
            any_time(lb__miniedit_get("time"))
            persistent.timeofday = lb__miniedit_get("time")
            if  persistent.timeofday == "prolog":
                persistent.timeofday =  "prologue"
            persistent.sprite_time = lb__miniedit_get("spritetime")


        lb__miniedit_mode = "edit"
        lb__miniedit_idx = 0
        lb__miniedit_upd_time()

        if  _preferences.language == "english":
            lb__miniedit_time_menu = [(u"Interface design and background filter?\n",None),(u"Winter","prolog"),(u"Summer, Day","day"),(u"Summer, Sunrise/Sunset","sunset"),(u"Summer, Night","night")]
            lb__miniedit_spritetime_menu = [(u"Characters lighting?\n",None),(u"Day","day"),(u"Sunrise/Sunset","sunset"),(u"Night","night")]
            lb__miniedit_bg_menu = [(u"Which background?\n",None),(u"Interior","int"),(u"Exterior","ext"),(u"Solid black","black"),(u"Solid white","white")]
            lb__miniedit_who_menu = [(u"Which character?\n",None)] + [(globals()[i+"_name"] if i+"_name" in globals() else i,i) for i in ["cs","dv","el","mi","mt","mz","pi","sh","sl","un","us","uv"]]
            lb__miniedit_say_menu = [(u"Who is saying?\n",None)] + [(u"Narrator","narrator"),(u"Semyon","me"),(u"Thoughts","th")] + [(globals()[i+"_name"],i) for i in ["cs","dv","el","mi","mt","mz","pi","sh","sl","un","us","uv"]]
        else:
            lb__miniedit_time_menu = [(u"Оформление интерфейса и фильтр фонов?\n",None),(u"Зима","prolog"),(u"Лето, День","day"),(u"Лето, Утро/Вечер","sunset"),(u"Лето, Ночь","night")]
            lb__miniedit_spritetime_menu = [(u"Подсветка спрайтов?\n",None),(u"День","day"),(u"Утро/Вечер","sunset"),(u"Ночь","night")]
            lb__miniedit_bg_menu = [(u"Какой фон?\n",None),(u"Интерьер","int"),(u"Экстерьер","ext"),(u"Чёрный","black"),(u"Белый","white")]
            lb__miniedit_who_menu = [(u"Который персонаж?\n",None)] + [(globals()[i+"_name"] if i+"_name" in globals() else i,i) for i in ["cs","dv","el","mi","mt","mz","pi","sh","sl","un","us","uv"]]
            lb__miniedit_say_menu = [(u"Кто говорит?\n",None)] + [(u"Рассказчик","narrator"),(u"Семён","me"),(u"Мысль","th")] + [(globals()[i+"_name"],i) for i in ["cs","dv","el","mi","mt","mz","pi","sh","sl","un","us","uv"]]
        lb__miniedit_pos = ["fleft","left","cleft","center","cright","right","fright"]
        lb__miniedit_cls = ["far","","close"]
        lb__miniedit_nightmare = ["dead","nohead","nightmare","burned","blood","zombie"]

    jump lb__miniedit_loop

init python:
    lb__miniedit_change = lambda mode: lambda: [globals().__setitem__("lb__miniedit_mode", mode),True][-1]
    lb__miniedit_change_idx = lambda mode,idx: lambda: [globals().__setitem__("lb__miniedit_mode", mode),globals().__setitem__("lb__miniedit_idx", idx),True][-1]

    def lb__miniedit_button(text=None, clicked=None, width=90, bgcolor=None):
        if  text is not None:
            ui.button(clicked=clicked, xpos=0, xanchor=0.0, ypos=0, xpadding=6, xminimum=width)
            ui.text(text, style="button_text", size=14)
        else:        
            ui.null(width=width)

    def lb__miniedit_export():
        text =  "    $ %s_time()\n" % lb__miniedit_get("time")
        text += "    $ persistent.sprite_time = \"%s\"\n" % lb__miniedit_get("spritetime")
        text += "    scene bg %s\n" % lb__miniedit_get("scene")
        for id,i in enumerate(lb__miniedit_get("show")):
            n_same = len([x for x in lb__miniedit_get("show")[:id+1] if x["who"] == i["who"] ])
            if  n_same == 1:
                text += "    show %s %s %s %s at %s\n" % (i["who"],i["emo"],i["dress"],i["close"],i["at"])
            else:
                text += "    show %s %s %s %s at %s as %s%d\n" % (i["who"],i["emo"],i["dress"],i["close"],i["at"],i["who"],n_same)
            if  i["who"] == "qr" and i["at"] == "center" and lb__miniedit_get("who") == "qr":
                text += "    show qrtext u\"%s\"\n" % lb__miniedit_get("what")
        if  lb__miniedit_get("who") == "narrator":
            text += "    \"%s\"\n" % (lb__miniedit_get("what"))
        else:
            text += "    %s \"%s\"\n" % (lb__miniedit_get("who"),lb__miniedit_get("what"))
        text += "\n"
        return text

    def lb__miniedit_inner_export():
        text =  " "*20 + "{\n"
        for x in ["time","spritetime","scene","who","what"]:
            text +=  " "*24 + '"%s": "%s",\n'%(x,lb__miniedit_get(x))
        text +=  " "*24 + '"show": [\n'
        for x in lb__miniedit_get("show"):
            text +=  " "*28 + '{"who":"%s","emo":"%s","dress":"%s","close":"%s","at":"%s"},\n'%(x["who"],x["emo"],x["dress"],x["close"],x["at"])
        text +=  " "*24 + '],\n' +  " "*20 + '},\n'
        return text

    def lb__miniedit_get_emos(who):
        emos = list(set([m[1] for m in renpy.display.image.images if len(m)>=2 and m[0] == who and m[-1] not in ["close","far"]]))
        return [k for k in sorted(emos) if k not in lb__miniedit_nightmare] + [k for k in sorted(emos) if k in lb__miniedit_nightmare]
        
    def lb__miniedit_get_dress(who, emo):
        sprites = [i for i in renpy.display.image.images if len(i)>1 and i[0] == who and i[1] == emo and i[-1] not in ["close","far"]]
        result = sorted([(" ".join(k)," ".join(k[2:])) for k in sprites])
        if  not lb__miniedit_allow_body:
            result = [(f,r) for f,r in result if r.find("body") == -1 ]
        if  not lb__miniedit_allow_full:
            result = [(f,r) for f,r in result if r.find("full") == -1 ]
        return [f for f,r in result], [r for f,r in result]
        

label lb__miniedit_loop:
    if  lb__miniedit_mode == "edit":
        scene expression ("bg "+lb__miniedit_get("scene"))
        python:
            for id,i in enumerate(lb__miniedit_get("show")):
                renpy.show(" ".join([i["who"],i["emo"],i["dress"],i["close"]]), at_list=[globals()[i["at"]]], tag="tag%d"%id)
                if  i["who"] == "qr" and i["at"] == "center" and lb__miniedit_get("who") == "qr":
                    renpy.show(("qrtext","u\"%s\""%lb__miniedit_get("what")), tag="tag_%d"%id)

        python:
            ui.vbox()
            ui.hbox()
            lb__miniedit_button()
            lb__miniedit_button("time@day")
            lb__miniedit_button(lb__miniedit_get("time"),lb__miniedit_change("time_edit"))
            ui.close()
            ui.hbox()
            lb__miniedit_button()
            lb__miniedit_button("sprites")
            lb__miniedit_button(lb__miniedit_get("spritetime"),lb__miniedit_change("spritetime_edit"))
            ui.close()
            ui.hbox()
            lb__miniedit_button()
            lb__miniedit_button("scene")
            lb__miniedit_button("bg")
            lb__miniedit_button(lb__miniedit_get("scene"),lb__miniedit_change("bg_edit"))
            ui.close()
            for i,item in enumerate(lb__miniedit_get("show")):
                ui.hbox()
                lb__miniedit_button("↑",lb__miniedit_change_idx("show_up",i) if i!=0 else None,30)
                lb__miniedit_button("X",lb__miniedit_change_idx("show_delete",i),30)
                lb__miniedit_button("↓",lb__miniedit_change_idx("show_down",i) if i+1!=len(lb__miniedit_get("show")) else None,30)
                lb__miniedit_button("show")
                lb__miniedit_button(item["who"])
                emos = lb__miniedit_get_emos(lb__miniedit_get("show")[i]["who"])
                lb__miniedit_button(width=30)
                lb__miniedit_button("-",lb__miniedit_change_idx("show_emo_minus",i) if len(emos) and item["emo"] != emos[0] else None,30)
                lb__miniedit_button(item["emo"], lb__miniedit_change_idx("show_emo",i) if len(emos) > 1 else None)
                lb__miniedit_button("+",lb__miniedit_change_idx("show_emo_plus",i) if len(emos) and item["emo"] != emos[-1] else None,30)
                lb__miniedit_button(width=30)
                fulldresses,dresses = lb__miniedit_get_dress(lb__miniedit_get("show")[i]["who"], lb__miniedit_get("show")[i]["emo"])
                lb__miniedit_button("-",lb__miniedit_change_idx("show_dress_minus",i) if len(dresses) and item["dress"] != dresses[0] else None,30)
                lb__miniedit_button(item["dress"],lb__miniedit_change_idx("show_dress",i) if len(dresses) > 1 else None)
                lb__miniedit_button("+",lb__miniedit_change_idx("show_dress_plus",i) if len(dresses) and item["dress"] != dresses[-1] else None,30)
                lb__miniedit_button(width=30)
                lb__miniedit_button("-",lb__miniedit_change_idx("show_close_minus",i) if item["close"] != lb__miniedit_cls[0] and item["who"] not in ["qr","ss","ss_che"] else None,30)
                lb__miniedit_button(item["close"])
                lb__miniedit_button("+",lb__miniedit_change_idx("show_close_plus",i) if item["close"] != lb__miniedit_cls[-1] and item["who"] not in ["qr","ss","ss_che"] else None,30)
                lb__miniedit_button(width=30)
                lb__miniedit_button("at",width=30)
                lb__miniedit_button("<",lb__miniedit_change_idx("show_at_minus",i) if item["at"] != lb__miniedit_pos[0] else None,30)
                lb__miniedit_button(item["at"])
                lb__miniedit_button(">",lb__miniedit_change_idx("show_at_plus",i) if item["at"] != lb__miniedit_pos[-1] else None,30)
                ui.close()
            ui.hbox()
            lb__miniedit_button()
            lb__miniedit_button("+ show",lb__miniedit_change("show_add"))
            ui.close()
            ui.hbox()
            lb__miniedit_button()
            lb__miniedit_button(lb__miniedit_get("who"),lb__miniedit_change("say_who_edit"))
            lb__miniedit_button(lb__miniedit_get("what"),lb__miniedit_change("say_what_edit"))
            ui.close()
            ui.null(height=20)
            ui.hbox()
            lb__miniedit_button(__("{b}КЛОНИРОВАТЬ{/b}"),lb__miniedit_change("clone_slot"))
            for i in range(len(persistent.lb__miniedit_slots)):
                lb__miniedit_button("%d"%i,lb__miniedit_change_idx("load_slot",i) if i != persistent.lb__miniedit_slot else None,29)
            lb__miniedit_button(__("{b}УДАЛИТЬ{/b}"),lb__miniedit_change("del_slot") if len(persistent.lb__miniedit_slots)>1 else None)
            ui.close()
            ui.hbox()
            lb__miniedit_button(__("{b}ЗАПУСТИТЬ{/b}"),lb__miniedit_change("run"))
            lb__miniedit_button(__("{b}КОПИРОВАТЬ КОД{/b}"),lb__miniedit_change("copy"))
            lb__miniedit_button(__("{b}ЭКСПОРТИРОВАТЬ{/b}"),lb__miniedit_change("export"))
            # lb__miniedit_button(__("{b}ЭКСПОРТИРОВАТЬ В СВОЁМ ФОРМАТЕ{/b}"),lb__miniedit_change("export_inner"))
            ui.close()
            ui.close()
        $ ui.interact()
    
    else:
        if lb__miniedit_mode == "load_slot":
            $ persistent.lb__miniedit_slot = lb__miniedit_idx
            $ lb__miniedit_upd_time()

        elif lb__miniedit_mode == "clone_slot":
            python:
                import copy
                persistent.lb__miniedit_slots.insert(persistent.lb__miniedit_slot+1, copy.deepcopy(persistent.lb__miniedit_slots[persistent.lb__miniedit_slot]))
                persistent.lb__miniedit_slot += 1
    
        elif lb__miniedit_mode == "del_slot":
            if layout.invoke_yesno_prompt(None, __("Удалить текущий слот?!")):
                python:
                    del persistent.lb__miniedit_slots[persistent.lb__miniedit_slot]
                    if  persistent.lb__miniedit_slot > 0:
                        persistent.lb__miniedit_slot -= 1
                    lb__miniedit_upd_time()
    
        elif lb__miniedit_mode == "run":
            scene expression ("bg "+lb__miniedit_get("scene"))
            python:
                for id,i in enumerate(lb__miniedit_get("show")):
                    renpy.show(" ".join([i["who"],i["emo"],i["dress"],i["close"]]), at_list=[globals()[i["at"]]], tag="tag%d"%id)
                    if  i["who"] == "qr" and i["at"] == "center" and lb__miniedit_get("who") == "qr":
                        renpy.show(("qrtext","u\"%s\""%lb__miniedit_get("what")), tag="tag_%d"%id)
                who = globals()[lb__miniedit_get("who")]
                what = lb__miniedit_get("what")
            who "%(what)s"
    
        elif lb__miniedit_mode == "copy":
            python:
                import pygame
                import pygame.scrap
                pygame.scrap.init()
                # TODO экспорт через encode("utf-8") не работает
                # При pygame.scrap информации в Сети почти нет, в RenPy идёт уже скомпилированная версия
                # Крайне странный workaround случайно найден тут: http://habrahabr.ru/sandbox/64061
                pygame.scrap.put("text/plain;charset=utf-8",lb__miniedit_export().encode("utf-16")) 
            if  _preferences.language == "english":
                "Code is copied to clipboard. Press Ctrl+V in your favourite text editor."
            else:
                "Код скопирован в буфер обмена. Нажмите Ctrl+V в любимом текстовом редакторе."

        elif lb__miniedit_mode == "export":
            python:
                if  not renpy.exists("mods/export"):
                    import os
                    os.mkdir("game/mods/export")
                if  not renpy.exists("mods/export/test_export.rpy"):
                    with open("game/mods/export/test_export.rpy","w") as f:
                        f.write(
u"""init:
    $ mods["test__export"] = u"Экспортировано из Мини-редактора"
    $ mod_tags["test__export"] = ["gameplay:vn","length:nano"]

translate english strings:
    old '""".encode("utf-8")
                            )
                        f.write(
u"""Экспортировано из Мини-редактора'
    new 'Exported from Mini-editor'

label test__export:
""".encode("utf-8")
                            )
                with open("game/mods/export/test_export.rpy","a") as f:
                    f.write(lb__miniedit_export().encode("utf-8")+"\n")
            if  _preferences.language == "english":
                "Exported to \"game/mods/export/test_export.rpy\". Restart the game to apply changes to that test mod."
            else:
                "Экспортировано в \"game/mods/export/test_export.rpy\". Перезагрузите игру чтобы применить изменения в том тестовом моде."

        elif lb__miniedit_mode == "export_inner":
            python:
                with open("export.txt","a") as f:
                    f.write(lb__miniedit_inner_export().encode("utf-8")+"\n")
    
        elif lb__miniedit_mode == "time_edit":
            python:
                lb__miniedit_set("time", lb_display_menu(lb__miniedit_time_menu))
                lb__miniedit_upd_time()
    
        elif lb__miniedit_mode == "spritetime_edit":
            python:
                lb__miniedit_set("spritetime", lb_display_menu(lb__miniedit_spritetime_menu))
                persistent.sprite_time = lb__miniedit_get("spritetime")
    
        elif lb__miniedit_mode == "bg_edit":
            python:
                where = lb_display_menu(lb__miniedit_bg_menu)
                if  where in ["black","white"]:
                    lb__miniedit_set("scene", where)
                else:
                    keys = [i[1] for i in renpy.display.image.images if i[0] == "bg" and i[1].startswith(where+"_") and i[1].find("_"+lb__miniedit_get("time")) != -1]
                    if  lb__miniedit_get("time") == "prolog":
                        keys += [i[1] for i in renpy.display.image.images if i[0] == "bg" and i[1].startswith(where+"_") and i[1].find("_winter") != -1]
                        keys += ["intro_xx","semen_room","semen_room_window"] if where == "int" else ["bus_stop"]
                    elif lb__miniedit_get("time") == "day":
                        keys += ["int_bus"] if where == "int" else ["ext_bus","ext_no_bus"]
                    elif lb__miniedit_get("time") == "night" and where == "int":
                        keys += ["int_bus_black","int_liaz"]
                        keys += [i[1] for i in renpy.display.image.images if i[0] == "bg" and i[1].startswith("int_mine") and i[1].find("_night") == -1]
                        keys += [i[1] for i in renpy.display.image.images if i[0] == "bg" and i[1].startswith("int_catacombs") and i[1].find("_night") == -1]
#                    res = lb_display_menu([("{size=-10}"+k+"{/size}",k) for k in sorted(keys)])

                    import math
                    n = int(math.ceil(math.sqrt(float(len(keys)))))
                    n = 2 if n == 1 else n
                    ui.grid(n,n)
                    for b in sorted(keys):
                        try:
                            ui.imagebutton(im.MatrixColor(im.FactorScale(ImageReference("bg "+b),1.0/n),im.matrix.saturation(0.3)),im.FactorScale(ImageReference("bg "+b),1.0/n),clicked=ui.returns(b))
                        except:
                            ui.button(clicked=ui.returns(b))
                            ui.text(b)
                    for b in range(n*n-len(keys)):
                        ui.null()
                    ui.close()
                    res = ui.interact()

                    lb__miniedit_set("scene", res)
    
        elif lb__miniedit_mode == "show_up":
            $ tmp = lb__miniedit_get("show")[lb__miniedit_idx-1]
            $ lb__miniedit_get("show")[lb__miniedit_idx-1] = lb__miniedit_get("show")[lb__miniedit_idx]
            $ lb__miniedit_get("show")[lb__miniedit_idx] = tmp
    
        elif lb__miniedit_mode == "show_delete":
            $ del lb__miniedit_get("show")[lb__miniedit_idx]
    
        elif lb__miniedit_mode == "show_down":
            $ tmp = lb__miniedit_get("show")[lb__miniedit_idx+1]
            $ lb__miniedit_get("show")[lb__miniedit_idx+1] = lb__miniedit_get("show")[lb__miniedit_idx]
            $ lb__miniedit_get("show")[lb__miniedit_idx] = tmp
    
        elif lb__miniedit_mode == "show_emo_minus":
            $ emos = lb__miniedit_get_emos(lb__miniedit_get("show")[lb__miniedit_idx]["who"])
            $ tmp = emos.index(lb__miniedit_get("show")[lb__miniedit_idx]["emo"]) - 1 if lb__miniedit_get("show")[lb__miniedit_idx]["emo"] in emos else 0
            $ lb__miniedit_get("show")[lb__miniedit_idx]["emo"] = emos[ tmp ]

        elif lb__miniedit_mode == "show_emo_plus":
            $ emos = lb__miniedit_get_emos(lb__miniedit_get("show")[lb__miniedit_idx]["who"])
            $ tmp = emos.index(lb__miniedit_get("show")[lb__miniedit_idx]["emo"]) + 1 if lb__miniedit_get("show")[lb__miniedit_idx]["emo"] in emos else 0
            $ lb__miniedit_get("show")[lb__miniedit_idx]["emo"] = emos[ tmp ]

        elif lb__miniedit_mode == "show_emo":
            python:
                keys = list(set([i[1] for i in renpy.display.image.images if len(i)>=2 and i[0] == lb__miniedit_get("show")[lb__miniedit_idx]["who"] and i[-1] not in ["close","far"]]))  
                tmp =  [(" ".join([lb__miniedit_get("show")[lb__miniedit_idx]["who"],k,"..."]),k) for k in sorted(keys) if k not in lb__miniedit_nightmare]
                tmp[-1] = (tmp[-1][0]+"\n",tmp[-1][1])
                tmp += [(" ".join([lb__miniedit_get("show")[lb__miniedit_idx]["who"],k,"..."]),k) for k in sorted(keys) if k in lb__miniedit_nightmare]
            $ lb__miniedit_get("show")[lb__miniedit_idx]["emo"] = lb_display_menu(tmp)
    
        elif lb__miniedit_mode == "show_dress_minus":
            $ fulldresses,dresses = lb__miniedit_get_dress(lb__miniedit_get("show")[lb__miniedit_idx]["who"], lb__miniedit_get("show")[lb__miniedit_idx]["emo"])
            $ tmp = dresses.index(lb__miniedit_get("show")[lb__miniedit_idx]["dress"]) - 1 if lb__miniedit_get("show")[lb__miniedit_idx]["dress"] in dresses else -1
            $ lb__miniedit_get("show")[lb__miniedit_idx]["dress"] = dresses[ tmp ]

        elif lb__miniedit_mode == "show_dress_plus":
            $ fulldresses,dresses = lb__miniedit_get_dress(lb__miniedit_get("show")[lb__miniedit_idx]["who"], lb__miniedit_get("show")[lb__miniedit_idx]["emo"])
            $ tmp = dresses.index(lb__miniedit_get("show")[lb__miniedit_idx]["dress"]) + 1 if lb__miniedit_get("show")[lb__miniedit_idx]["dress"] in dresses else -1
            $ lb__miniedit_get("show")[lb__miniedit_idx]["dress"] = dresses[ tmp ]

        elif lb__miniedit_mode == "show_dress":
            $ fulldresses,dresses = lb__miniedit_get_dress(lb__miniedit_get("show")[lb__miniedit_idx]["who"], lb__miniedit_get("show")[lb__miniedit_idx]["emo"])
            $ lb__miniedit_get("show")[lb__miniedit_idx]["dress"] = lb_display_menu(zip(fulldresses,dresses))
    
        elif lb__miniedit_mode == "show_close_minus":
            $ lb__miniedit_get("show")[lb__miniedit_idx]["close"] = lb__miniedit_cls[lb__miniedit_cls.index(lb__miniedit_get("show")[lb__miniedit_idx]["close"])-1]
    
        elif lb__miniedit_mode == "show_close_plus":
            $ lb__miniedit_get("show")[lb__miniedit_idx]["close"] = lb__miniedit_cls[lb__miniedit_cls.index(lb__miniedit_get("show")[lb__miniedit_idx]["close"])+1]
    
        elif lb__miniedit_mode == "show_at_minus":
            $ lb__miniedit_get("show")[lb__miniedit_idx]["at"] = lb__miniedit_pos[lb__miniedit_pos.index(lb__miniedit_get("show")[lb__miniedit_idx]["at"])-1]
    
        elif lb__miniedit_mode == "show_at_plus":
            $ lb__miniedit_get("show")[lb__miniedit_idx]["at"] = lb__miniedit_pos[lb__miniedit_pos.index(lb__miniedit_get("show")[lb__miniedit_idx]["at"])+1]
    
        elif lb__miniedit_mode == "show_add":
            python:
                lb__miniedit_idx = len(lb__miniedit_get("show"))
                tmp = {}
                tmp["who"] = lb_display_menu(lb__miniedit_who_menu)
                tmp["emo"] = "normal" if tmp["who"] not in ["un_old","ss_che"] else "serious" if tmp["who"] in ["un_old"] else ""
                tmp["dress"] = "pioneer" if tmp["who"] not in ["pi","uv","cs","qr","un_old","ss","ss_che"] else "plat1" if tmp["who"] in ["un_old"] else "fancy" if tmp["who"] in ["ss"] else ""
                tmp["close"] = ""
                tmp["at"] = "center"
                lb__miniedit_set("show", lb__miniedit_get("show")+[tmp])
    
        elif lb__miniedit_mode == "say_who_edit":
            $ lb__miniedit_set("who", lb_display_menu(lb__miniedit_say_menu))
    
        elif lb__miniedit_mode == "say_what_edit":
            if  _preferences.language == "english":
                $ lb__miniedit_set("what", renpy.input("Text to say:",lb__miniedit_get("what")))
            else:
                $ lb__miniedit_set("what", renpy.input("Текст реплики:",lb__miniedit_get("what")))
    
        else:
            $ renpy.error(("Unknown mode",lb__miniedit_mode))

        $ lb__miniedit_mode = "edit"

    jump lb__miniedit_loop

init python:
    def lb_display_menu(items):
        return renpy.display_menu(items, screen="lb_simple_choice")

screen lb_simple_choice:
    modal True
    python:
        choice_colors_hover={                        
                'day': "#9dcd55",
                'night': "#3ccfa2",
                'sunset': "#dcd168",
                'prologue': "#98d8da"
                                    }
        
        choice_colors={
                'day': "#466123",
                'night': "#145644",
                'sunset': "#69652f",
                'prologue': "#496463"
                                    }
        
        choice_colors_selected={                        
                    'day': "#2a3b15",
                    'night': "#0b3027",
                    'sunset': "#42401e",
                    'prologue': "#2d3d3d",
                                }
    window:
        background Frame(get_image("gui/choice/"+persistent.timeofday+"/choice_box.png"),50,50)
        xfill True
        yalign 0.5
        left_padding 75
        right_padding 75
        bottom_padding 50
        top_padding 50
        vbox:
            xalign 0.5
            for caption, action, chosen  in items:
                if action and caption:
                    button:
                        background None
                        action action
                        text caption:
                            font "fonts/corbel.ttf"
                            size 37
                            hover_size 37
                            color choice_colors[persistent.timeofday]
                            hover_color choice_colors_hover[persistent.timeofday]
                            xcenter 0.5
                else:
                    text caption:
                        font "fonts/corbel.ttf"
                        size 37
                        color choice_colors[persistent.timeofday]
