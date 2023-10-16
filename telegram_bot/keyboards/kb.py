from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

menu = [
    [
        InlineKeyboardButton(
            text="📝 Посмотреть топ книг", callback_data="get_data"
        ),
        InlineKeyboardButton(
            text="🖼 Добавить свою книгу ", callback_data="generate_image"
        ),
    ],
    [
        InlineKeyboardButton(
            text="💳 Активные книги ", callback_data="buy_tokens"
        ),
        InlineKeyboardButton(text="💰  Мой профиль", callback_data="balance"),
    ],
    [
        InlineKeyboardButton(text="🔎 Помощь", callback_data="help"),
        InlineKeyboardButton(text="Регистрация", callback_data="auth"),
    ],
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True
)
iexit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]
    ]
)
