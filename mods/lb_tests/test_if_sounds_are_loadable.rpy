init:
    $ tests_to_run["test_if_sounds_are_loadable"] = u"Are all play statements using existing filenames?"

init python:
    def test_if_sounds_are_loadable_inner(item, lst):
        result = True
        for f in lst:
            LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"Checking for file: " + `f`,"paranoic")
            if  not isinstance(f, basestring):
                LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"Not a string object: " + `f`,"error")
                result = False
            elif  not renpy.loadable(f):
                LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"Can't load file: " + `f`,"error")
                result = False
            else:
                LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"File " + `f` + " really exists","paranoic")
        return result

    def test_if_sounds_are_loadable():
        result = True
        for (k,item) in ( (k, renpy.game.script.namemap[k]) for k in sorted(renpy.game.script.namemap.keys()) ):
            if  isinstance(item,renpy.ast.UserStatement):
                parsed = renpy.statements.parse(item, item.line, item.block)
                if  parsed[0][0] == "play":
                    channel = parsed[0][1] if len(parsed[0]) > 1 else renpy.python.py_eval(parsed[1]["channel"]) if "channel" in parsed[1] else None
                    if  not channel or not renpy.music.channel_defined(channel):
                        LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"Wrong sound/music channel name: " + channel,"error")
                        result = False
                        continue
                    try:
                        f = renpy.python.py_eval(parsed[1]["file"])
                    except:
                        LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"Can't eval python string: " + parsed[1]["file"],"error")
                        result = False
                        continue
                    result = test_if_sounds_are_loadable_inner(item, f if isinstance(f, list) else [f]) and result
        return result


    
