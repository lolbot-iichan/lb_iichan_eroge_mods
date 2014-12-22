init:
    $ filters["image__naked"] = u"Голое Лето"

translate english strings:
    old "Голое Лето"
    new "Naked Summer"

python early:
    def image__naked():
        for id in (id for id in renpy.display.image.images if len(id) >= 2):
            naked_id = id[:-1]+(u"body",) if id[-1] not in ["close","far"] else id[:-2]+(u"body",id[-1])
            if  naked_id != id and naked_id in renpy.display.image.images:
                renpy.image(id, ImageReference(naked_id))
