from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from .keyboards import * 

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Привет {message.from_user.full_name}, я бот продавец ключей для игр \n чем могу помочь?""",reply_markup=menu_kb)

# @router.message(F.text.lower() == 'привет')
# async def hello(message: Message):
#     await message.answer('Привет, как дела?')

# @router.message(F.text.startswith('пока'))
# async def byebye(message: Message):
#     await message.answer('До свидания ')

@router.message(F.text == 'Категории') 
async def categories(message: Message): 
    await message.answer('Выберите категорию:',reply_markup= await categories_kb()) 

@router.message(F.text == 'Все игры') 
async def games(message: Message): 
    await message.answer('Выберите игру:')


@router.message(Command("help"))
async def help(message: Message):
    await message.answer('<h1> dice </h1> hello')
 

@router.callback_query(F.data.startswith('category_'))
async def category_game(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer('Игры по этой категории: ',
        reply_markup=await games_kb(category_id))
    
from database.queryset import get_game

@router.callback_query(F.data.startswith('game_'))
async def game(callback: CallbackQuery):
    game_id = callback.data.split('_')[1]
    game = await get_game(game_id)
    if game.image.startswith('http') or game.image.startswith('AgAC'):
        image = game.image
    else:
        image = FSInputFile(game.image)
    await callback.message.answer_photo(photo=image,caption=f'{game.name} \n {game.description}'
                           )

# Напишите кнопку для покупки в детальной информации о игре
# В кнопке должно находиться колличество ключей (50) и сумма в $
# Кнопка находиться под описанием к игре