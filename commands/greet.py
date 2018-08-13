import random

grs = ['Welcome labmem 00%NUM%, %USER%!', 'Welcome to the Future Gadget Laboratory, %USER%',
       '%USER%... I see you\'ve arrived', 'Welcome, assistant of mine, %USER%!',
       'You\'ve arrived in the delta worldline, %USER%', 'Welcome %USER%, or should I say *Za Zombie*']


def out(id):
    g = random.choice(grs)
    g = g.replace('%USER%', '<@' + id + '>')
    g = g.replace('%NUM', str(random.randrange(1, 9)))
    return g