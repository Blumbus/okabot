import discord
import os
from commands import *
from settings import *
from private import *
import random

test_live = False # a test_ bool, True if project is running live and hosted
if test_live:
    token = os.environ['token']
else:
    token = private_vars.t1 + private_vars.t2

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    serv = message.server.id
    chan = message.channel.id
    if serv not in config.servers:
        return

    usrs = message.mentions
    primary = message.author
    message.content = message.content.lower().strip()
    print('Raw content: ' + message.content)
    if len(usrs) > 0:
        primary = usrs[0]
    words = []
    words = message.content.split()
    if message.content.startswith(config.command_prefix):
        message.content = message.content[1:].strip()
        words[0] = words[0][1:]
        for user in message.mentions:
            for i in range(0, len(words)):
                if words[i] == '<@' + user.id + '>' or words[i] == '<@!' + user.id + '>':
                    words[i] = user
        new_words = []
        bracc_start = -1
        curr_word = ''
        for i in range(0, len(words)):
            if isinstance(words[i], discord.User):
                new_words.append(words[i])
            elif words[i].startswith('[') and bracc_start == -1:
                if words[i].endswith(']'):
                    new_words.append(words[i][1:-1])
                else:
                    curr_word = words[i][1:]
                    bracc_start = i
            elif bracc_start != -1:
                if words[i].endswith(']'):
                    curr_word += ' ' + words[i][:-1]
                    bracc_start = -1
                    new_words.append(curr_word)
                else:
                    curr_word += ' ' + words[i]
            else:
                new_words.append(words[i])
        words = new_words

        if command_perms(message, words[0]):
            if words[0] == 'pickup' or words[0] == 'flirt':
                await client.send_message(message.channel, pickup.out(stringify_words(words)))
            elif words[0] == 'ship':
                if len(words) < 2:
                    await client.send_message(message.channel, 'Please specify at least one thing to ship.')
                else:
                    if len(words) == 2:
                        print('1 arg')
                        thing1 = message.author
                        thing2 = words[1]
                    else:
                        print('2 args')
                        thing1 = words[1]
                        thing2 = words[2]
                    await client.send_message(message.channel, ship.out(thing1, thing2))
            elif words[0] == 'rate':
                if (len(words)) < 2:
                    await client.send_message(message.channel, 'You\'ll have to give me something to rate.')
                else:
                    await client.send_message(message.channel, rate.out(words[1:]))
            elif words[0] == 'ask':
                await client.send_message(message.channel, ask.out(words[1:]))
        else:
            print('permission denied in channel!')
    if command_perms(message, 'chat'):
        test_content = message.content = message.clean_content.lower().strip()
        print(test_content)
        if 'good bot' in test_content:
            await client.send_message(message.channel, 'Good Alpacaman.')
        elif 'bad bot' in test_content:
            await client.send_message(message.channel, 'Bad Alpacaman.')


def stringify_words(words):
    for w in words:
        if isinstance(w, discord.User):
            w = str(w.id)
    return words

def command_perms(msg, cmd):
    perm = cmd
    if perm not in config.servers[msg.server.id]['commands']:
        perm = 'default'
    if config.servers[msg.server.id]['commands'][perm] == 'all':
        return True
    if msg.channel.id in config.servers[msg.server.id]['commands'][perm]['white']:
        return True
    return False

@client.event
async def on_member_join(member):
    ch = config.servers[member.server.id]['greet']
    if ch in config.servers[member.server.id]['commands']['greet']['white']:
        await client.send_message(member.server.get_channel(ch), greet.out(member.id))

@client.event
async def on_ready():
    print('Hououin Kyouma has arrived!')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await  client.change_presence(game=discord.Game(name='with world lines'))

client.run(token)