from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'самая длинная река К-Р?'
    answers = [
        "нил",
        "Нарын",
        "Чу",
        "Чаткал?",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Учи географию",
        open_period=15,
        reply_markup=markup
    )


# @dp.callback_query_handler(lambda call: call.data == 'button_call_3')
async def quiz_3(call: types.CallbackQuery):
    question = 'Кто стал лучшим ментором в прошлом месяце по BEKEND!'
    answers = [
        "канат",
        "асыл",
        "гулина",
        "марлен",
        "вова"
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation=" ай ай ай",
        open_period=15
    )


def callback_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
