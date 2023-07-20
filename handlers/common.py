from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет, я бот, который будет давать тебе краткую информацию"
                         " из википедии о том, что ты мне напишешь.Если будут вопросы напиши команду /help")


@start_router.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer("1: Если в википедии не будет конкретно того слова которое"
                         "  ты напишешь, то выведится информация\n\n"
                         "1.1: Об однокоренном слове\n\n "
                         "1.2: Выведится сообщение с выбором,"
                         " где можно   посмотреть информацию о запрошенном слове\n\n"
                         " 2: Если сообщение с информацией будет слишком большим,  то"
                         " выведится сообщение до определенного лимита  символов и кнопка Читать полностью"
                         " где можно дочитать  информацию ")


@start_router.message(Command('delete_menu'))
async def handle_menu_delete(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Вы удалили меню(((')
