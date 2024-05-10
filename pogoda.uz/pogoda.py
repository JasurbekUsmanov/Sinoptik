from confi import token
from aiogram import Dispatcher,F,Bot
from aiogram.types import Message
import asyncio
from aiogram.filters.command import Command
from confi import token
from aiogram.types import Message,CallbackQuery
from button import vaqt,button
from bs4 import BeautifulSoup as X
import requests

dp = Dispatcher()
bot = Bot(token=token)

@dp.message(Command("start"))
async def start(message:Message):
      await message.answer(f"Assalomu aleykum {message.from_user.full_name}\nXush qelibsiz bizning botimizga\nNecha kunlik Havo qo'rmoqchisiz",reply_markup=vaqt)


@dp.message(F.text =="Haftalik")
async def hafta(message:Message):
      await message.answer("Qaysi viloyatni haftalik obu havosini qo'rmochisiz",reply_markup=button)
      
@dp.callback_query(F.data)
async def haftatemp(call:CallbackQuery):
      text = call.data
      http = "https://sinoptik.ua/погода-"
      ht=http+text
      url = requests.get(ht)
      html_t=X(url.content,"html.parser")
      a = html_t.select("#content")
      await call.message.answer(f"Viloyat:{text}")
      for i in a:
            for j in range(7):
                  await call.message.answer(f"📅Kun:{i.select('.date')[j].text}\n🗓Oy:{i.select('.month')[j].text}\n🌡Eng katta bo'lish mumkun bolgan harorat:{i.select(".max")[j].text}\n🌡Eng kichik bo'lish mumkun bolgan harorat:{i.select('.min')[j].text}")
@dp.message(F.text == "Kunlik")
async def kunlik(message:Message):
      url = requests.get("https://sinoptik.ua/погода-ургенч")
      
      html_t = X(url.content,"html.parser")
      a = html_t.select("#content")
      await message.answer("Bugungi kunni ko'rsatmalar")
      for i in a:
            await message.answer(f"Qaysi kunliki:{i.select(".day-link")[0].text}\n📅Kun:{i.select('.date')[0].text}\n🗓Oy:{i.select('.month')[0].text}\n🌡Eng katta bo'lish mumkun bolgan harorat:{i.select(".max")[0].text}\n🌡Eng kichik bo'lish mumkun bolgan harorat:{i.select('.min')[0].text}")      
                  
            





async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("bot Faoliayatini to'xtadi")
