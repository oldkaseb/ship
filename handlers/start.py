from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    if message.chat.type != "private":
        return
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📋 راهنما", callback_data="help"),
        InlineKeyboardButton("📞 تماس با مالک", url="https://t.me/oldkaseb"),
        InlineKeyboardButton("➕ افزودن به گروه", url=f"https://t.me/{(await bot.get_me()).username}?startgroup=true")
    )
    await message.answer(
        "👋 به ربات شیپر فضوله خوش اومدی!\n"
        "✨ با امکانات حرفه‌ای کراش و کاپل و پنل مدیریتی\n"
        "💸 شارژ ماهیانه: ۵۰ هزار تومان\n"
        "🆓 تست رایگان ۷ روزه برای هر گروه",
        reply_markup=kb
    )
