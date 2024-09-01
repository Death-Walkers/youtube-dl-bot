from aiogram import types
from youtubesearchpython import VideosSearch


def get_results_kb(results: VideosSearch) -> types.InlineKeyboardMarkup:
    buttons = [
        [
            types.InlineKeyboardButton(
                text=result.get("title"),
                callback_data=f"https://www.youtube.com/watch?v={result.get('id')}",
            )
        ]
        for result in results.resultComponents
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def get_dl_kb(video_url: str) -> types.InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="🎵 Скачать аудио", callback_data=f"audiodl_{video_url}")],
        [types.InlineKeyboardButton(text="🖼 Скачать превью", callback_data=f"thumbnaildl_{video_url}")],
        [types.InlineKeyboardButton(text="❌ Удалить это сообщение", callback_data="delete_message")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
