from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from database.queryset import * 

menu_kb = ReplyKeyboardMarkup(
    keyboard = [[KeyboardButton(text='Категории')], [KeyboardButton(text = 'Все игры')]], resize_keyboard=True, input_field_placeholder='Выберите пункт меню', one_time_keyboard=True
)

# inline_test = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Аркада', callback_data='button1')],
#                                                     [InlineKeyboardButton(text='Шутер', callback_data='button2')],
#                                                     [InlineKeyboardButton(text='Гонки', callback_data='button3')]])

async def categories_kb():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text=category.name,
            callback_data=f'category_{category.id}'
        ))
    return builder.adjust(2).as_markup()