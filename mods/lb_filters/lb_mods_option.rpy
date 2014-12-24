init:
    $ filters["ui__mods_raise"] = u"Поднять строку Модов в меню настроек"

translate english strings:
    old "Поднять строку Модов в меню настроек"
    new "Raise Mods button in preferences menu"

init python:
    def ui__mods_raise():
        opts = renpy.display.screen.screens[("preferences",None)]
        win = opts.ast.children[-1].children[-1].children[0].children[0]
        for ch in win.children:
            if  ch.displayable.__module__ == "renpy.ui" and ch.displayable.__name__ == "_textbutton":
                if  ch.positional == [u'translation["mods"][_preferences.language]']:
                    win.children.insert(0,win.children.pop(win.children.index(ch))) 
                    break
