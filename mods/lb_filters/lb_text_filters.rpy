init:
    $ filters["text__nya_kawaii"] = u"Кавайное Лето"
    $ filters["text__no_r"] = u"Картавое Лето"
    $ filters["text__blah"] = u"Грязное Лето"

translate english strings:
    old "Кавайное Лето"
    new "Kawaii Summer"
    old "Картавое Лето"
    new "Dyslalia Summer"
    old "Грязное Лето"
    new "Damn Summer"

python early:
    import re, random
    def lb__custom_say(f, lst, s, who, what, interact=True):
        for i in lst:
            if  "who" in i and who not in i["who"]:
                continue
            if  "lang" in i and _preferences.language not in i["lang"]:
                continue
            what = f(what,i["in"],i["out"])
        s(who, what, interact)
    def lb__txt(f,lst):
        s = renpy.exports.say
        renpy.exports.say = lambda who, what, interact=True: lb__custom_say(f, lst, s, who, what, interact=interact)

    def lb__regexp_replace(what, before, after):
        return re.sub(before, after, what)
    def lb__random_replace(what, before, afters):
        parts = what.split(before)
        result = parts[0]
        for part in parts[1:]:
            result += random.choice(afters) + part
        return result

    text__nya_kawaii = lambda: lb__txt(lb__regexp_replace,[
            {"lang":["english"], "in":ur'([^.,?!…\'"])…',  "out":u'\\1, unyu…'},
            {"lang":["english"], "in":ur'([^.,?!…\'"])\.', "out":u'\\1, nya.'},
            {"lang":["english"], "in":ur'([^.,?!…\'"])!',  "out":u'\\1, nipah!'},
            {"lang":["english"], "in":ur'([^.,?!…\'"])\?', "out":u'\\1, nyoro~n?'},
            {"lang":[None],      "in":ur'([^.,?!…\'"])…',  "out":u'\\1, унью…'},
            {"lang":[None],      "in":ur'([^.,?!…\'"])\.', "out":u'\\1, ня.'},
            {"lang":[None],      "in":ur'([^.,?!…\'"])!',  "out":u'\\1, нипа!'},
            {"lang":[None],      "in":ur'([^.,?!…\'"])\?', "out":u'\\1, нёро~н?'},
        ])
    text__blah       = lambda: lb__txt(lb__random_replace,[
            {"lang":["english"], "in":",", "out":[u' as shit,',u', damn it,',u', holy cow,',u', fucking',u', I\'m tellin\' ya,']+[u',']*3, "who":['th','me',None]},
            {"lang":[None],      "in":",", "out":[u', мать его,',u' нахрен,',u', чёрт побери,',u', мля,',u', это самое,',u' в натуре,',u', в рот мне ноги,']+[u',']*3, "who":['th','me',None]},
        ])

    text__no_r       = lambda: lb__txt(lb__regexp_replace,[
            {"in":ur'р', "out":u'г', "who":['me']},
            {"in":ur'Р', "out":u'Г', "who":['me']},
            {"in":ur'r', "out":u'g', "who":['me']},
            {"in":ur'R', "out":u'g', "who":['me']},
        ])


