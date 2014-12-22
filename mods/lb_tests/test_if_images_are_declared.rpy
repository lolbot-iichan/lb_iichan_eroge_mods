init:
    $ tests_to_run["test_if_images_are_declared"] = u"Are all show/scene using declared image objects?"

init python:
    def test_if_images_are_declared():
        result = True
        for (k,item) in ( (k, renpy.game.script.namemap[k]) for k in sorted(renpy.game.script.namemap.keys()) ):
            if  (isinstance(item,renpy.ast.Scene) or isinstance(item,renpy.ast.Show)) and item.imspec and isinstance(k,tuple) and len(k) == 3:
                LOG(u"Item is "+`(k,item)`,"paranoic")

                zorder = 0
                expression = None
                tag = None
                behind = []
                if len(item.imspec) == 3:
                    iname, at_list, layer = item.imspec
                elif len(item.imspec) == 6:
                    iname, expression, tag, at_list, layer, zorder = item.imspec
                elif len(item.imspec) == 7:
                    iname, expression, tag, at_list, layer, zorder, behind = item.imspec
                LOG(u"Checking "+`iname`,"paranoic")

                if  not expression:
                    if  renpy.display.image.images.has_key(iname):
                        LOG(u"Found some image in renpy.display.image.images: "+`iname`,"paranoic")
                    elif  renpy.display.image.images.has_key(iname[:-1]) and isinstance(renpy.display.image.images[iname[:-1]],renpy.text.extras.ParameterizedText):
                        LOG(u"Found ParameterizedText in renpy.display.image.images: "+`iname[:-1]`,"paranoic")
                    else:
                        result = False
                        LOG(u"(%s:%s) "%(item.filename,item.linenumber)+"Image not declared: "+" ".join(iname),"error")
                else:
                        LOG(u"(%s:%s) "%(item.filename,item.linenumber)+u"TODO: Expression is used: "+`iname`,"warning")
        return result

        