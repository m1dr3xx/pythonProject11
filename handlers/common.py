from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет, я бот, который будет давать тебе краткую информацию из википедии о том, что ты мне напишешь.Если будут вопросы напиши команду /help")  # Отвечаем на полученное сообщение

@start_router.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer("Если в википедии не будет конкретно того слова которое ты напишешь то выведится информация либо об однокоренном слове либо не выведится вовсе")