import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN') # 8420270855:AAF7Ral1S9xtCd-nqQgCUgHKIO8MwKP2k_A

dp = Dispatcher()




# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.reply(f"Hello ! {message.from_user.first_name}")

@dp.message(Command('help'))
async def help_information(message: Message):
    await message.answer(f'username = {message.from_user.username}')

@dp.message(F.text == 'test')
async def magicflter(message: Message):
    await message.answer(f'username = {message.from_user.username}')



# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


