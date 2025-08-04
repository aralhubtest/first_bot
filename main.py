import asyncio
import os
from dotenv import load_dotenv
import logging


from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboars import keyboard_single_row

# Configure logging
logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # 8420270855:AAF7Ral1S9xtCd-nqQgCUgHKIO8MwKP2k_A

dp = Dispatcher()


photo_id = ""


async def sum_numbers(a: int, b: int):
    return a + b


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.reply(
        text=f"Hello ! {message.from_user.first_name}", reply_markup=keyboard_single_row
    )


@dp.message(Command("help"))
async def help_information(message: Message):
    await message.answer_video(
        "BAACAgIAAxkBAAPLaJBLFOKmoU8v8HABiMLMjB5OdawAArt-AAJ2LYhIh9LHhReHhFg2BA"
    )


@dp.message(F.text == "test")  # if text == test
async def magicflter(message: Message):
    await message.answer(f"chat_id = {message.chat.id}")


@dp.message(F.photo)
async def handle_photo(message: Message) -> None:
    await message.answer("Спасибо за фото!")


@dp.message(F.sticker)
async def handle_sticker(message: Message) -> None:
    await message.answer("Классный стикер!")


@dp.message(F.voice)
async def handle_voice(message: Message) -> None:
    await message.answer("Я получил голосовое сообщение.")


@dp.message(F.location)
async def handle_location(message: Message) -> None:
    await message.answer(
        f"Ваши координаты: {message.location.latitude},{message.location.longitude}"
    )


@dp.message(F.text == "Кнопка 1")
async def hello(soobsheine: Message):
    await soobsheine.answer_photo(photo="AgACAgIAAxkBAAN8aJBGMPeNirxKZ3M3Gzc3I2V8QmYAAr_xMRsnMoFIsOyygxKuiWoBAAMCAAN4AAM2BA", caption='Babur Developer')


@dp.message()  # if True
async def echo(message: Message):
    await message.answer(message.text[::-1])


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
