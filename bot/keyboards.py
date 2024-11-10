"""
Keyboards
"""

from aiogram import types


def get_options_keyboard(url: str) -> types.InlineKeyboardMarkup:
    """Returns a keyboard with options what to do with the video"""
    buttons = [
        [types.InlineKeyboardButton(text="🎥 Скачать видео (Только shorts)", callback_data=f"videodl_{url}")],
        [types.InlineKeyboardButton(text="🎵 Скачать аудио", callback_data=f"audiodl_{url}")],
        [types.InlineKeyboardButton(text="🖼 Скачать превью", callback_data=f"thumbnaildl_{url}")],
        [types.InlineKeyboardButton(text="❌ Удалить это сообщение", callback_data="delete_message")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
