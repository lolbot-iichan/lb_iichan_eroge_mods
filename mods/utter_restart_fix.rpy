screen lb_filters_fix:
    textbutton translation["apply"][_preferences.language]:
        style "log_button"
        text_style "settings_link"
        yalign 0.92
        xalign 0.9
        action (Function(stop_music), Function(renpy.quit,relaunch=True))

init python:
    ch = renpy.display.screen.screens[("filters",None)].ast.children[-1].children
    if  ch[-1].displayable.__module__ == "renpy.ui" and ch[-1].displayable.__name__ == "_textbutton":
        if  ch[-1].positional == [u'translation["apply"][_preferences.language]']:
            ch[-1] = renpy.display.screen.screens[("lb_filters_fix",None)].ast.children[-1]