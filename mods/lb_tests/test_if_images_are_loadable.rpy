init:
    $ tests_to_run["test_if_images_are_loadable"] = u"Are all image declarations using existing filenames?"

init python:
    def test_if_images_are_loadable_try_predict(what, item):
        LOG(u"Calling item.predict_files() for item:"+`what`,"paranoic")
        try:
            predicted = item.predict_files()
            return predicted, True
        except Exception, e:
            LOG(u"(%s) "%(" ".join(what)) + "Failed to call item.predict_files(): " +`e` ,"error")
            return [], False

    def test_if_images_are_loadable_collect_img(what, item):
        if  hasattr(item,"predict_files"):
            return test_if_images_are_loadable_try_predict(what,item)
        elif hasattr(item,"child") and hasattr(item.child,"function") and item.child.function.func_name == "condition_switch_show":
            preds = [test_if_images_are_loadable_collect_img(what,sub) for (cond,sub) in item.child.args[0]]
            predicted = set(sum([list(p[0]) for p in preds],[]))
            res = len([p[1] for p in preds if not p[1]]) == 0
            return predicted, res
        elif isinstance(item,(renpy.text.extras.ParameterizedText, renpy.display.imagelike.Solid, renpy.display.layout.MultiBox)):
            LOG(u"Ignoring item "+`what`+" with a known type","paranoic")
            return [], True
        else:
            LOG(u"TODO: Item "+`what`+" does not have method predict_files():"+`item`,"warning") # TODO think of something for ATL images
            return [], True

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
        for (what,item) in ( (k, renpy.display.image.images[k]) for k in sorted(renpy.display.image.images.keys()) ):
            predicted, res = test_if_images_are_loadable_collect_img(what,item)
            result = test_if_images_are_loadable_inner(what,predicted) and res and result
        return result
    
