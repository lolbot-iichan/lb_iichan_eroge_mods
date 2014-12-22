init:
    $ filters["widget__filename"] = u"Текущая строка кода"
    $ filters["widget__music"] = u"Текущая музыка"
    $ filters["widget__images"] = u"Текущие изображения"

translate english strings:
    old "Текущая строка кода"
    new "Current source line"
    old "Текущая музыка"
    new "Current music"
    old "Текущие изображения"
    new "Current images"

init python:
    widget_overlay_set = []
    widget__filename = lambda: widget_overlay_set.append(("src",widget__filename_inner))
    widget__music    = lambda: widget_overlay_set.append(("♪♫♬",widget__music_inner))
    widget__images   = lambda: widget_overlay_set.append(("img",widget__images_inner))

    def widget__filename_inner():
        import os
        fullfn, line = renpy.get_filename_line()
        return [ "%s:%d" % (os.path.basename(fullfn), line) ]

    def widget__music_inner():
        m = renpy.music.get_channel("music").get_playing()
        if  m:
            return [ m.split("/")[-1].replace(".ogg","").replace(".mp3","") ]
        return []

    def widget__images_inner():
        return [" ".join(x.name) for x in renpy.display.core.scene_lists().layers["master"]]

init 9999 python:
    if  widget_overlay_set:
        def editoverlay():
            ui.vbox(xpos=config.screen_width, xanchor=1.0, ypos=2)
            for  k,f in widget_overlay_set:
                for v in f():
                    ui.hbox()
                    ui.button(clicked=None, xpadding=6, xminimum=50)
                    ui.text(k, style="button_text", size=14)
                    ui.button(clicked=None, xpadding=6, xminimum=300)
                    ui.text(v, style="button_text", size=14)
                    ui.close()
            ui.close()
        config.overlay_functions.append(editoverlay)
        