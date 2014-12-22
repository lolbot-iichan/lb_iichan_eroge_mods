init:
    $ filters["ui__mods_raise"] = u"Поднять строку Модов в меню настроек"

translate english strings:
    old "Поднять строку Модов в меню настроек"
    new "Raise Mods button in preferences menu"

init python:
    def ui__mods_raise():
        opts = renpy.display.screen.screens[("preferences",None)]
        win = opts.ast.children[-1].children[-1].children[0].children[0]
        win.children.insert(0,win.children.pop(22)) 
        