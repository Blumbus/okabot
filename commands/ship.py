import random
import discord

def out(thing1, thing2):
    name1 = thing1
    name2 = thing2
    disp1 = thing1
    disp2 = thing2
    if isinstance(thing1, discord.User):
        name1 = thing1.id
        disp1 = thing1.display_name
    if isinstance(thing2, discord.User):
        name2 = thing2.id
        disp2 = thing2.display_name
    v = sum(ord(x) for x in name1) + sum(ord(x) for x in name2)
    random.seed(v)
    r = (random.random() + random.random()) * 50
    print(r)
    val = round(r)
    ret = '**' + str(disp1) + '** and **' + str(disp2) + '**... a ' + str(val) + '% ship rate!\n'
    if val > 95:
        ret += 'A love that transcends time and space! They\'re perfect!'
    elif val > 80:
        ret += random.choice(['These numbers! This must be the will of Steins Gate', 'A pair as good as Kurisu and DkPepper!'])
    elif val > 60:
        ret += random.choice(['Impressive... perhaps these two have met before somewhere'])
    elif val > 40:
        ret += random.choice(['Not bad, I\'m sure they could bond over omurice and catgirls', 'Maybe they have a promising future... but I won\'t tell! Fwuuhahaha!'])
    elif val > 20:
        ret += random.choice(['Doesn\'t look so good... perhaps we can change that', 'Maybe Daru can give them some daring tips...'])
    else:
        ret += random.choice(['Ouch...', 'Even a time leap can\'t fix this'])
    return ret
