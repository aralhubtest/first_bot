import asyncio
import os
from dotenv import load_dotenv
import logging
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, chat
from generate_qr import generate as qr_gen
from keyboars import keyboard_single_row
from test_api import get_weather
from aiogram.fsm.state import State, StatesGroup


class FormCity(StatesGroup):
    city = State() # Состояние для запроса имени

class FormUrl(StatesGroup):
    url = State()


class FormCar(StatesGroup):
    marka = State()
    year = State()
    country = State()
    color = State()
    gear_box = State()




logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # 8420270855:AAF7Ral1S9xtCd-nqQgCUgHKIO8MwKP2k_A
# Инициализация хранилища в памяти
storage = MemoryStorage()
# При инициализации Dispatcher передайте ему хранилище
dp = Dispatcher(storage=storage)
bot = Bot(token=TOKEN)

# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.reply(
        text=f"Hello ! {message.from_user.first_name}", reply_markup=None)


@dp.message(Command('get_weather'))
async def ask_city(message: Message, state: FSMContext):
    await state.set_state(FormCity.city)
    await message.answer('Название города?')

@dp.message(FormCity.city)
async def wheather(message: Message):
    data = await get_weather(message.text)
    response_text = (f'gorod: {data.name}\n'
    f'temperatura:{data.temp}\n'
    f'pogoda:{data.weather}\n'
    f'samal tezligi:{data.wind_speed}\n'
    f'seziledi kak:{data.feels_like}'
    if data else 'Onday gorod joq')
    await message.reply(text=response_text)


@dp.message(Command('generate_qr'))
async def ask_url(message: Message, state: FSMContext):
    await state.set_state(FormUrl.url)
    await message.answer('Укажите ссылку')




@dp.message(FormUrl.url)
async def generate(message: Message):
    output_file_path = qr_gen(message.text, file_path=f'qr_{message.from_user.id}.png')
    photo = FSInputFile(output_file_path)
    await message.answer_photo(photo=photo, caption=message.text)


@dp.message(Command('newpost'))
async def start_state(message: Message, state: FSMContext):
    await state.set_state(FormCar.marka)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.answer('marka?')

@dp.message(FormCar.marka)
async def set_marka(message: Message, state: FSMContext):
    await state.update_data(marka=message.text)
    await state.set_state(FormCar.color)
    await message.answer('Color?')


@dp.message(FormCar.color)
async def set_color(message: Message, state: FSMContext):
    await state.update_data(color=message.text)
    await state.set_state(FormCar.year)
    await message.answer('Year?')

@dp.message(FormCar.year)
async def set_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(FormCar.country)
    await message.answer('Country?')

@dp.message(FormCar.country)
async def set_country(message: Message, state: FSMContext):
    await state.update_data(country=message.text)
    await state.set_state(FormCar.gear_box)
    await message.answer('Gear box', reply_markup=keyboard_single_row)

@dp.message(FormCar.gear_box)
async def set_gear_box(message: Message, state: FSMContext):
    await state.update_data(gear_box=message.text)
    data_car = await state.get_data()
    await message.answer(f'Marka - {data_car['marka']}\nYear - {data_car['year']}\nColor - {data_car['color']}')

# Run the bot
async def main() -> None:

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
