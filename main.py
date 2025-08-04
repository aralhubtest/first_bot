import asyncio
import os
from dotenv import load_dotenv
import logging


from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


# Configure logging
logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # 8420270855:AAF7Ral1S9xtCd-nqQgCUgHKIO8MwKP2k_A

dp = Dispatcher()


async def sum_numbers(a: int, b: int):
    return a + b


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.reply(f"Hello ! {message.from_user.first_name}")


@dp.message(Command("help"))
async def help_information(message: Message):
    await message.answer_photo('AgACAgIAAxkBAANtaJBDsYT9o7upw9i2LS9FAwM8bDsAArDxMRsnMoFIjjwd50VUF7EBAAMCAANzAAM2BA')

@dp.message(F.text == "test") # if text == test
async def magicflter(message: Message):
    await message.answer(f"chat_id = {message.chat.id}")


@dp.message(F.photo)
async def hello(soobsheine: Message):
    await soobsheine.reply(f'id = {soobsheine.photo[-1].file_id} - size = {soobsheine.photo[-1].file_size} uniqid = {soobsheine.photo[-1].file_unique_id}')
    await soobsheine.reply(f'id = {soobsheine.photo[0].file_id} - size = {soobsheine.photo[0].file_size} uniqid = {soobsheine.photo[0].file_unique_id}')


@dp.message() #if True
async def echo(message: Message):
    await message.answer(message.text[::-1])


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
