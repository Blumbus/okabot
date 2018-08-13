import random
import discord
import datetime

triggers = ['gnight', 'gn', 'gnite', 'goodnite', 'goodnight']

last = 0

def trigger(words):
    for t in triggers:
        if t in words or t + '!' in words:
            return True
    return False

ans = ['Sleep well labmem! :okabeSip:', 'Goodnight! :okabeSip:', 'Gn! :okabeSip:', 'See you tomorrow! :okabeSip:']

def out(words):
    ret = ''
    global last
    dt = datetime.datetime.now()
    if last == 0 or (dt - last).seconds / 60 > 5:
        last = dt
        ret = random.choice(ans)
    return ret