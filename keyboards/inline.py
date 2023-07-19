from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_url_keyboard(message_text: str):
    yandex = InlineKeyboardButton(text='in Yandex', url=f"https://yandex.ru/search/?clid=2186621&text={message_text}")
    google = InlineKeyboardButton(text='in Google', url=f'google.com/search?q={message_text}')

    links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [yandex, google]
    ])
    return links_keyboard
