from aiogram import Router
from aiogram.types import Message
from wikipedia import wikipedia

wiki_router = Router()

@wiki_router.message()
async def wiki(message: Message):
    await message.answer(str(wikipedia.search(message.text)))