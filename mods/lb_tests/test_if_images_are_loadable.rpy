init:
    $ tests_to_run["test_if_images_are_loadable"] = u"Are all image declarations using existing filenames?"

init python:
    def test_if_images_are_loadable_inner(what, lst):
        LOG(u"Checking "+`what`+":"+`lst`,"paranoic")
        result = True
        for f in lst:
            if  not renpy.loadable(f):
                result = False
                LOG(u"(%s) "%(" ".join(what)) + "File is not loadable: " + f,"error")
        return result

    def test_if_images_are_loadable():
        result = True
        for (k,item) in ( (k, renpy.display.image.images[k]) for k in sorted(renpy.display.image.images.keys()) ):
            if  hasattr(item,"predict_files"):
                result = test_if_images_are_loadable_inner(k,item.predict_files()) and result
            elif hasattr(item,"child") and hasattr(item.child,"function") and item.child.function.func_name == "condition_switch_show":
                result = test_if_images_are_loadable_inner(k,set(sum([sub.predict_files() for (cond,sub) in item.child.args[0]],[]))) and result
            elif isinstance(item,(renpy.text.extras.ParameterizedText, renpy.display.imagelike.Solid, renpy.display.layout.MultiBox)):
                LOG(u"Ignoring item "+`k`+" with a known type","paranoic")
            else:
                LOG(u"TODO: Item "+`k`+" does not have method predict_files():"+`item`,"warning") # TODO think of something for ATL images
        return result


    
