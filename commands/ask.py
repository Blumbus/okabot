import random
import discord
import datetime

ans = ['Steins;Gate wills it', 'Absolutely', 'I think  my supa hacka could answer that better than I can',
       'Unfortunately, no', 'No...', 'Is a gelnana slimy?', 'I doubt it', 'It\'s possible...',
       'Not in this worldline', 'That\'s up to you', 'Don\'t let the Organization find out but... yes',
       'Hah, in your dreams']

def out(words):
    return random.choice(ans)