init:
    $ filters["ui__mods_menu"] = u"Расширенное меню выбора модов"

translate english strings:
    old "Расширенное меню выбора модов"
    new "Extended mods selection menu"
    old "Применено фильтров: %d"
    new "Filters applied: %d"
    old "Найдено модов: %d"
    new "Mods found: %d"
    old "Текущий набор фильтров тэгов сохранён.{fast}"
    new "Current set of tag filters is saved.{fast}"

init python:
    def ui__mods_menu():
        renpy.display.screen.screens[("mods",None)] = renpy.display.screen.screens[("mods_by_lb",None)]






init 9000 python:
    if  not persistent.mods_filter:
        persistent.mods_filter = {"+":[], "-":[]}

init 9000 python:
    for m in mods:
        if  not m in mod_tags:
            mod_tags[m] = ["special:tag_me"]
# uncomment to auto-add authors as tags
#        mod_tags[m] += ["author:"+m.split("__")[0] if m.find("__")!=-1 else "author:unknown"]
    for m in mod_tags:
        if  not m in mods:
            del mod_tags[m]
    tag_mods = {t:[m for m in mods if t in mod_tags[m]] for t in set(sum(mod_tags.values(),[]))}

screen mods_by_lb:
    timer 0.01 action Start("prepare_env")

label prepare_env:
    $ renpy.music.stop()
    $ set_mode_adv()
    $ init_map_zones()
    if  hasattr(renpy.store,"make_names_known"):
        $ make_names_known()
    $ skip_text_blocks = False
    $ font_size="small"
    $ day_time()
    scene bg black

    jump mods_selection

label mods_selection:
    $ copy_persistent_to_mods()
    jump mods_selection_loop

init python:
    def copy_persistent_to_mods():
        global mods_filter
        import copy
        mods_filter = copy.deepcopy(persistent.mods_filter)  
    
    def copy_mods_to_persistent():
        import copy
        persistent.mods_filter = copy.deepcopy(mods_filter)  
    
    def filter_mods_list(lst):
        res = []
        for i in lst:
            ok = True
            for p in mods_filter["+"]:
                if  i not in tag_mods[p]:
                    ok = False
            for p in mods_filter["-"]:
                if  i in tag_mods[p]:
                    ok = False
            if ok:
                res += [i]
        return res

    def img_bar(name, color, x=None, y=None):
        rv = theme.OneOrTwoColor("_roundrect/rr" + name + ".png", color)
        return rv if x is None else Frame(rv, x, y, tile=True)
    style.futaba_button = Style(style.button)
    style.futaba_button.color = "#8E0000"
    style.futaba_button.background = Frame("mods/lb_mod_selection/futaba_button.png",6,6)
    style.futaba_button.hover_background = Frame(im.MatrixColor("mods/lb_mod_selection/futaba_button.png",im.matrix.contrast(2)),6,6)
    style.futaba_button.insensitive_background = Frame(im.Grayscale("mods/lb_mod_selection/futaba_button.png"),6,6)
    style.futaba_vscrollbar = Style(style.vscrollbar)
    style.futaba_vscrollbar.bottom_bar       = img_bar("vscrollbar",       "#EEAA88", 0, 12)
    style.futaba_vscrollbar.top_bar          = img_bar("vscrollbar",       "#EEAA88", 0, 12)
    style.futaba_vscrollbar.thumb            = img_bar("vscrollbar_thumb", "#EEAA88")
    style.futaba_vscrollbar.hover_bottom_bar = img_bar("vscrollbar",       "#FFD591", 0, 12)
    style.futaba_vscrollbar.hover_top_bar    = img_bar("vscrollbar",       "#FFD591", 0, 12)
    style.futaba_vscrollbar.hover_thumb      = img_bar("vscrollbar_thumb", "#FFD591")

label mods_selection_loop:
    python:
        ui.window(yalign=0,xpos=700,xanchor=1.0,xfill=True,yfill=True,background="#F0E0D6")
        ui.null()
        ui.window(yalign=0,xpos=700,xanchor=0.0,xfill=True,yfill=True,background="#FFFFEE")
        ui.null()

        what_filters = [(k,len(filter_mods_list(v))) for k,v in tag_mods.iteritems() if k not in mods_filter["+"] and len(filter_mods_list(v))]
        what_mods = [(k, "{color=#117743}[[%s]{/color} %s" %( "{{?}" if k.find("__") == -1 else k.split("__")[0], __(mods[k]) )) for k in filter_mods_list(mods.keys())]

        what_filter_groups = sorted(list(set([i.split(":")[0] for i,n in what_filters if i.find(":")!=-1])))

        vp_tags = ui.viewport(mousewheel=True,xpos=35,ypos=0,xmaximum=700)
        ui.vbox(xmaximum=600)
        ui.hbox()
        ui.button(clicked=ui.returns(("*",)),style="futaba_button")
        ui.text("★",style="futaba_button")
        ui.text(__("Применено фильтров: %d")%len(sum(mods_filter.values(),[])),color="#8E0000")
        ui.close()
        for t in mods_filter:
            for name in sorted(mods_filter[t]):
                ui.hbox(xpos=35)
                ui.button(clicked=ui.returns(("X",t,name)),style="futaba_button")
                ui.text("X",style="futaba_button")
                ui.button(xfill=True,right_margin=100-35,style="futaba_button")
                ui.text("%s %s"%(t,name),style="futaba_button")
                ui.close()
        ui.text(__("Найдено модов: %d")%len(what_mods),color="#8E0000")
        for g in what_filter_groups:
            ui.text(g+":",color="#8E0000",xpos=35)
            for name,n in sorted(what_filters):
                if  name.startswith(g+":"):
                    ui.hbox(xpos=70)
                    ui.button(clicked=ui.returns(("-",name)),style="futaba_button")
                    ui.text("-",style="futaba_button")
                    ui.button(clicked=ui.returns(("+",name)),style="futaba_button")
                    ui.text("+",style="futaba_button")
                    ui.button(xfill=True,right_margin=100,style="futaba_button")
                    ui.text("%s (%d)"%(name.split(":")[-1],n),style="futaba_button")
                    ui.close()
        ui.close()
        if  len(what_filters)+len(what_filter_groups) > 36:
            ui.bar(adjustment=vp_tags.yadjustment, xpos=20, style='futaba_vscrollbar')

        vp_mods = ui.viewport(mousewheel=True, xpos=820,ypos=0 if len(what_mods)>37 else (3+540*(37-len(what_mods))/37),xmaximum=1000)
        ui.vbox(xmaximum=1200)
        for lbl,name in sorted(what_mods,key=lambda (i,j):(j,i)):
            ui.button(xfill=True,clicked=ui.jumps(lbl),style="futaba_button")
            ui.text(name,style="futaba_button")
        ui.close()
        if  len(what_mods) > 37:
            ui.bar(adjustment=vp_mods.yadjustment, xpos=800, style='futaba_vscrollbar')

        res = ui.interact()
        if  isinstance(res,tuple) and res[0] in ["+","-"]:
            mods_filter[res[0]] += [res[1]]
        if  isinstance(res,tuple) and res[0] in ["X"]:
            mods_filter[res[1]].remove(res[2])
        if  isinstance(res,tuple) and res[0] in ["*"]:
            copy_mods_to_persistent()
            renpy.exports.say(None, __(u"Текущий набор фильтров тэгов сохранён.{fast}"))
    jump mods_selection_loop
