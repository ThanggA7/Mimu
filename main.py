import discord
from discord.ext import commands, tasks
import asyncio
import os
import json
import random
import alive

bot = commands.Bot(command_prefix='!', self_bot=True)

# Tải cấu hình từ tệp tin JSON
with open('config.json') as config_file:
  config = json.load(config_file)

# Lấy các giá trị cấu hình từ đối tượng JSON
ID_CHANNEL = config['ID_CHANNEL']
LIST_SCAM = config['LIST_SCAM']
LIST_RANDOM_GAME = config['LIST_RANDOM_GAME']
LIST_TX = config['LIST_TX']
count1 = config['count1']
count2 = config['count2']
count3 = config['count3']
count4 = config['count4']
count5 = config['count5']


@bot.event
async def on_ready():
  print("-------------------------------")
  print(f'Đã đăng nhập vào acc: {bot.user.name}')
  print(f'ID: {bot.user.id}')
  print("-------------------------------")
  try:
    await main()
  except Exception as e:
    print(f"An error occurred: {e}")


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
  global ID_SCAM
  await bot.wait_until_ready()
  while not bot.is_closed():
    channel = bot.get_channel(ID_CHANNEL)
    ID_SCAM = random.choice(LIST_SCAM)
    await channel.send(f'.scam <@{ID_SCAM}>')
    await asyncio.sleep(915)
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


async def keobuabao():
  global count4
  global LIST_RANDOM_GAME
  await bot.wait_until_ready()
  while not bot.is_closed():
    channel = bot.get_channel(ID_CHANNEL)
    GAME = random.choice(LIST_RANDOM_GAME)
    await channel.send(f'{GAME}')
    await asyncio.sleep(3)
    count4 += 1
    print(f"{bot.user.name} Đã ra {GAME} thành công lần {count4} ")
    print("-------------------------------")


async def taixiu():
  global count5
  global LIST_TX
  await bot.wait_until_ready()
  while not bot.is_closed():
    channel = bot.get_channel(ID_CHANNEL)
    TX = random.choice(LIST_TX)
    await channel.send(f'{TX}')
    await asyncio.sleep(500)
    count5 += 1
    print(
      f"{bot.user.name} chơi {TX} lần {count5} và không biết anh ấy giờ như thế nào :))) "
    )
    print("-------------------------------")


async def main():
  tasks = [scam, cauca, muaveso, keobuabao, taixiu]
  await asyncio.gather(*[task() for task in tasks])


alive.alive()
bot.run(os.environ.get('TOKEN'))
