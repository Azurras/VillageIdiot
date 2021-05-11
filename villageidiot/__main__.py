#!/usr/bin/env python3

import logging
import os
import random
from os.path import abspath, dirname, join

import discord
from discord.ext import commands
from discord.utils import find
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')  # Sets prefix for the bot commands


@bot.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {bot.user}')  # notification of login.
    await bot.change_presence(activity=discord.Game(name='Buttered Toast'))


@bot.event
async def on_message(message):
    # Needed to make sure prefix commands are still captured by the program.
    await bot.process_commands(message)
    await log_message(message)
    await check_for_poop_message(message)


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'introductions',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}!'.format(guild.name))


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'introductions',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Left {}!'.format(guild.name))


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='test', help='test command')
async def test_bot_command(ctx):
    await ctx.send("test")


@bot.command(name='discord_user', help='Sends a list of all users regardless of online status')
async def get_users_by_discord_name(ctx):
    users = ""
    for user in bot.users:
        users += str(user) + "\n"
    await ctx.send(users)


@bot.command(name='users', help='Sends a list of all users regardless of online status')
async def get_users_by_username(ctx, *arg):
    response = ""
    user_list = await get_users(ctx)
    if(len(arg) > 1):
        response = await get_users_category(arg, user_list)
    else:
        response = generate_user_output(user_list)
    await ctx.send(response)


@bot.command(name='online_users', help='Sends a list of all users regardless of online status')
async def send_user_list(ctx):
    users = ""
    emojis = bot.get_all_emojis
    print(emojis)
    await ctx.send(users)


@bot.command(name='poohead_caleb', help='Sends a list of all users regardless of online status')
async def send_caleb_message(ctx):
    for user in bot.users:
        # if("Azurras" in user.name):
        #user = bot.get_user(userM.id)
        await user.send("Eat ass")


async def check_for_poop_message(message):
    if message.author == bot.user:
        return
    if("poop" in message.content):
        response = f"{message.author.name}, there will be no talk of shit in here!"
        await message.channel.send(response)


@bot.command(name='exit')
@commands.has_role('admin')
async def close_bot(ctx):
    await bot.close()


def generate_user_output(user_list):
    user_response = ""
    for user in user_list:
        user_response += "%s\n" % user.name
    response = f"ALL USERS:\n{user_response}"

    return response


async def get_users(ctx):
    user_list = []
    for guild in bot.guilds:
        for member in guild.members:
            user_list.append(member)

    return user_list


async def get_users_category(arg, user_list):
    users = []
    users_str = ''
    for user in user_list:
        if(str(arg[0]) == "role"):
            for role in user.roles:
                if(str(arg[1]) == str(role)):
                    users.append(user.name)
                    users_str += "%s\n" % user.name
                    break
        elif arg == "status":
            if(str(arg[1]) == str(user.status)):
                users.append(user.name)
                users_str += "%s\n" % user.name

    response = f"Users (%s = %s):\n\n%s" % (
        str(arg[0]), str(arg[1]), users_str)

    return response


async def log_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")


def main():
    logging.basicConfig(filename='villageidiotlocator.log', level=logging.INFO)

    dotenv_path = join(dirname(dirname(abspath(__file__))), '.env')
    load_dotenv(dotenv_path)
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)  # Send token to bot object


if __name__ == "__main__":
    main()
