from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет, я бот, который будет давать тебе ссылку на википедию о том, что ты мне напишешь.")  # Отвечаем на полученное сообщение

