import discord
from discord.ext import commands, tasks
import asyncio
import os
import alive
from time import time

bot = commands.Bot(command_prefix='!', self_bot=True)
count1 = 0
count2 = 0
count3 = 0
ID_CHANNEL = 1096659409918230609
ID_SCAM = 615185168621371411

@bot.event
async def on_ready():
    print("-------------------------------")
    print(f'Logged in as {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print("-------------------------------")
    await main()
        
async def cauca():
    global count1
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(ID_CHANNEL)
        await channel.send('.cauca')
        await asyncio.sleep(16)
        count1 += 1
        print(f"{count1}: {bot.user.name} Đã câu cá thành công")
        print("-------------------------------")
async def scam():
    global count2
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(ID_CHANNEL)
        await channel.send(f'.scam {ID_SCAM}')
        await asyncio.sleep(900)
        count2 += 1
        print(f"{bot.user.name} Đã scam {ID_SCAM} thành công lần {count2} ")
        print("-------------------------------")
async def muaveso():
    global count3
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(ID_CHANNEL)
        await channel.send('.muaveso')
        await asyncio.sleep(43200)
        count3 += 1
        print(f"{bot.user.name} Đã muaveso thành công lần {count3} ")
        print("-------------------------------")
async def main():
    tasks = [scam(), cauca(), muaveso()]
    await asyncio.gather(*tasks)

alive.alive()
bot.run(os.environ.get('TOKEN'))
