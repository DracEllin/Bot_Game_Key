from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from .keyboards import *

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Привет {message.from_user.full_name}, я бот продавец ключей для игр \n чем могу помочь?""", reply_markup=menu_kb)

# @router.message(F.text.lower() == 'привет')
# async def hello(message: Message):
#     await message.answer('Привет, как дела?')

# @router.message(F.text.startswith('пока'))
# async def byebye(message: Message):
#     await message.answer('До свидания')

@router.message(F.text == 'Категории')
async def categories(message: Message):
    await message.answer('Выберите категорию:', reply_markup=await categories_kb())

@router.message(F.text == 'Все игры')
async def games(message: Message):
    await message.answer('Выберите игру:')


@router.message(Command("help"))
async def help(message: Message):
    await message.answer('<h1> dice </h1> hello')

# Напишите команду phone которая отвечает и даёт номер телефона

