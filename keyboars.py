from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание кнопок
button_1 = KeyboardButton(text="Mexanika")
button_2 = KeyboardButton(text="Automat")

# Создание клавиатуры с одной кнопкой в ряду
keyboard_single_row = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2]],
    resize_keyboard=True, # Изменяет размер клавиатуры под контент
    one_time_keyboard=True, # Скрывает клавиатуру после использования
    #input_field_placeholder="Выберите действие..." # Подсказка в поле ввода
)
