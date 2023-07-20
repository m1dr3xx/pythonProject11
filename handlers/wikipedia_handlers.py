from aiogram import Router
from aiogram.types import Message
from wikipedia import wikipedia, WikipediaException

from keyboards.inline import generate_url_keyboard

wiki_router = Router()


@wiki_router.message()
async def wiki(message: Message):
    try:
        answer = wikipedia.summary(str(message.text))
        if len(answer) <= 4096:
            await message.answer(wikipedia.summary(str(message.text)))
        else:
            shortened = answer[:4096 - 62 - len(message.text) - 10] + '...'
            await message.answer(shortened + f'\n<a href="https://ru.wikipedia.org/wiki/{message.text}">Читать полностью</a>')

    except WikipediaException:
        await message.answer("По данному запросу ничего не было найдено в википедии")
        await message.answer("Можете найти в интернете по ссылкам:", reply_markup=generate_url_keyboard(message.text))
