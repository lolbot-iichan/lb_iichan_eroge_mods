init:
    $ mods["lb__tests_start"] = u"Запуск юнит-тестов"
    $ mod_tags["lb__tests_start"] = ["gameplay:other","translation:english"]

translate english strings:
    old "Запуск юнит-тестов"
    new "Run unit tests"

init -9000 python:
    tests_to_run = {}

init python:
    LOG_LEVELS_STYLE = {"always":"ALW: %s", "error":"ERR: %s", "info":"INF: %s", "warning":"WRN: %s", "debug":"DBG: %s", "paranoic":"PRN: %s"}
    LOG_LEVELS_SAY_STYLE = {"always":"{color=FFF}%s{/color}", "error":"{color=F00}%s{/color}", "info":"{color=0F0}%s{/color}"}
    LOG_LEVELS_SAY  = ["always", "error", "info"]
    LOG_LEVELS_FILE = ["always", "error", "info", "warning", "debug"]

    def LOG(l, lvl):
        if  lvl in LOG_LEVELS_STYLE:
            l = LOG_LEVELS_STYLE[lvl] % l
        if  lvl in LOG_LEVELS_FILE:
            with open("out.log","a") as f:
                l = re.sub(ur'{color=[^}]*}', u'', l.replace("{/color}",""), flags=re.UNICODE)
                f.write(l.encode("utf-8")+"\n")
        if  lvl in LOG_LEVELS_SAY:
            if  lvl in LOG_LEVELS_SAY_STYLE:
                l = LOG_LEVELS_SAY_STYLE[lvl] % l
            ui.label(l, substitute=False)
    
label lb__tests_start:
    scene bg int_clubs_male_sunset
    python:
        import os
        if  os.path.exists("out.log"):
            os.unlink("out.log")

        test_n_fail = 0
        test_n_success = 0

        ui.window()
        ui.viewport(draggable=True, mousewheel=True)
        ui.vbox()
        LOG(u"You can scroll current log with mouse. It is also saved to out.log file with more details.", "info")

        for id in tests_to_run:
            t = getattr(store, id)
            LOG(u"Running test '" + t.func_name + "' (" + tests_to_run[id] + ")...", "always")
            result = t()
            if  result:
                test_n_success += 1
                LOG(u"Test '" + t.func_name + "' result is SUCCESS", "info")
            else:
                test_n_fail += 1
                LOG(u"Test '" + t.func_name + "' result is FAIL", "error")

        LOG(u"Tests succeeded: %d/%d" % (test_n_success,len(tests_to_run)), "info" if test_n_success else "always")
        LOG(u"Tests failed: %d/%d" % (test_n_fail,len(tests_to_run)), "error" if test_n_fail else "always")
        LOG(u"Done running tests...","always")

        ui.close()
        ui.interact()
        