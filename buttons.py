from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
share_contact=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Share Contact',request_contact=True)
        ]
    ]
)