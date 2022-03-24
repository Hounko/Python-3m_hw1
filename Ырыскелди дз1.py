from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def question_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Нет",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    button_call_2 = InlineKeyboardButton("Да",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    await bot.send_message(message.chat.id, 'Смог ли ты решить задачу?', reply_markup=markup)


@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def answer(call: types.CallbackQuery):
    answer1 = 'for i in list1:' \
            'list1.append(i)' \
            'if len(list1) == 8/12/6:' \
            'break'
    await bot.send_message(call.message.chat.id, answer1)

@dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def answer(call: types.CallbackQuery):
    answer2 = "Вы молодец!"
    await bot.send_message(call.message.chat.id, answer2)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)