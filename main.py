import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
from aiogram.filters import Command
from aiogram.types import Message

# ========== КОНФИГ ==========
BOT_TOKEN = "8674608099:AAG_Brb5RNwWwGc3jx_t1SyNqu4NHNRu8KE"

# Включаем логи
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ========== ОБРАБОТЧИКИ ==========

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎰 Привет! Это тестовый бот-казино.\n\n"
        "💰 Оплата через Telegram Stars.\n"
        "🔥 Команда /buy — купить тестовый товар за 1 Star."
    )

@dp.message(Command("buy"))
async def buy(message: Message):
    user_id = message.from_user.id
    
    # Создаем инвойс на 1 Star
    await bot.send_invoice(
        chat_id=user_id,
        title="🎲 Тестовая покупка",
        description="Покупка тестового товара за 1 Telegram Star",
        payload=f"test_payment_{user_id}",
        provider_token="",          # пустая строка = Stars
        currency="XTR",             # XTR = Telegram Stars
        prices=[LabeledPrice(label="⭐ 1 Star", amount=1)],
        start_parameter="test_buy"
    )

# Обработка успешной оплаты (исправленный синтаксис для aiogram 3.x)
@dp.message(lambda message: message.successful_payment is not None)
async def successful_payment(message: Message):
    payment = message.successful_payment
    stars = payment.total_amount
    
    await message.answer(
        f"✅ Оплата успешно проведена!\n"
        f"💰 Списано: {stars} Star{'ов' if stars > 1 else ''}\n"
        f"🎉 Товар зачислен (тестовый режим)."
    )

# ========== ЗАПУСК ==========
async def main():
    print("🚀 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())