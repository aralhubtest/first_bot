import asyncio
import os
from dotenv import load_dotenv
import logging


from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from generate_qr import generate as qr_gen
# from keyboars import keyboard_single_row
from test_api import get_weather


logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # 8420270855:AAF7Ral1S9xtCd-nqQgCUgHKIO8MwKP2k_A

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.reply(
        text=f"Hello ! {message.from_user.first_name}", reply_markup=None)


@dp.message(F.text == 'Кнопка 1')
async def generate(message: Message):
    output_file_path = qr_gen(message.text, file_path=f'qr_{message.from_user.id}.png')
    photo = FSInputFile(output_file_path)
    await message.answer_photo(photo=photo, caption=message.text)


@dp.message()
async def wheather(message: Message):
    data = await get_weather(message.text)
    response_text = (f'gorod: {data.name}\n'
    f'temperatura:{data.temp}\n'
    f'pogoda:{data.weather}\n'
    f'samal tezligi:{data.wind_speed}\n'
    f'seziledi kak:{data.feels_like}'
    if data else 'Onday gorod joq')
    await message.reply(text=response_text)


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
