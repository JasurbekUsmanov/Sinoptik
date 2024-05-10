from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton


button = InlineKeyboardMarkup(
      inline_keyboard=[
            [InlineKeyboardButton(text="Andijon viloyati",callback_data="андижон"),InlineKeyboardButton(text="Buxoro viloyati",callback_data="бухара")],
            [InlineKeyboardButton(text="Farg'ona viloyati",callback_data="фергана"),InlineKeyboardButton(text="Jizzax viloyati",callback_data="джизак")],
            [InlineKeyboardButton(text="Xorazm viloyati",callback_data="хорезм"),InlineKeyboardButton(text="Namangan viloyati",callback_data="наманган")],
            [InlineKeyboardButton(text="Navoiy viloyati",callback_data="навои"),InlineKeyboardButton(text="Qashqadaryo viloyati",callback_data="кашкадарья")],
            [InlineKeyboardButton(text="Toshkent viloyati",callback_data="ташкент"),InlineKeyboardButton(text="Samarqand viloyati",callback_data="самарканд")],
            [InlineKeyboardButton(text="Sirdaryo viloyati",callback_data="сырдарья"),InlineKeyboardButton(text="Surxondaryo viloyati",callback_data="гулистан")]
      ]
)
vaqt = ReplyKeyboardMarkup(
      keyboard=[
            [KeyboardButton(text="Haftalik"),KeyboardButton(text="Kunlik")]
      ],resize_keyboard=True
)