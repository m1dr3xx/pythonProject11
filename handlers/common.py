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
    await message.answer("Если в википедии не будет конкретно того слова которое"
                         " ты напишешь, то выведится информация"
                         " либо об однокоренном слове, либо выведится сообщение с выбором,"
                         " где можно посмотреть информацию о запрошенном слове,"
                         " либо если сообщение с информацией будет слишком большим, то"
                         " выведится ссылка на сайт с википедией запрошенного слова")

@start_router.message(Command('delete_menu'))
async def handle_menu_delete(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer('Вы удалили меню(((')

