from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from database.queryset import *

menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Категории')],[KeyboardButton(text ='Все игры')]
],resize_keyboard=True,input_field_placeholder='Выберите пункт меню',
                              one_time_keyboard=True)

# inline_test = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Аркада',callback_data='button1')],
#     [InlineKeyboardButton(text='Шутер',callback_data='button2')],
#     [InlineKeyboardButton(text='Аркада',callback_data='button3')]
    
# ])

async def categories_kb():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data= f'category_{category.id}' #== 'category_1'
        ))
    return builder.adjust(2).as_markup()

async def categories_kb2():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data= f'category2_{category.id}' #== 'category2_1'
        ))
    return builder.adjust(2).as_markup()

async def games_kb(category_id):
    builder = InlineKeyboardBuilder()
    games = await get_games(category_id)
    for game in games:
        builder.add(InlineKeyboardButton(
            text = game.name,
            callback_data= f'game_{game.id}' #== 'game_1'
        ))
    return builder.adjust(2).as_markup()
