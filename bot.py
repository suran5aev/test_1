from aiogram import Bot, Dispatcher, types , executor
import random
from config import token
bot = Bot(token=token)
dp = Dispatcher(bot)

number = random.randint(1,3)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Я загадал число от 1 до 3 угадайте')

@dp.message_handler(text = '1')
async def start(message:types.Message):
    if number == 1:
        await message.reply('Правильно вы отгадали')


    elif number != 1:
        await message.reply('Вы не отгадали')


@dp.message_handler(text = '2')
async def start(message:types.Message):
    if number == 2:
        await message.reply('Правильно вы отгадали')
       

    elif number != 2:
        await message.reply('Вы не отгадали')
       


@dp.message_handler(text = '3')
async def start(message:types.Message):
    if number == 3:
        await message.reply('Правильно вы отгадали')
       

    elif number != 3:
        await message.reply('Вы не отгадали')
       


executor.start_polling(dp)
