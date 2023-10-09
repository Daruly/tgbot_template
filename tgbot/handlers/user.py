from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.types import Message
import logging
from logging.handlers import RotatingFileHandler
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# from typing import Union

# from aiogram import Dispatcher, types, Bot
# from aiogram.types import Message, CallbackQuery
# from aiogram.dispatcher.filters import Command
# from tgbot.config import load_config
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
# from bot import dp
# from tgbot.keyboards.menu_keyboards import categories_keyboard, subcategories_keyboard, items_keyboard, item_keyboard, \
#     menu_cd

# from tgbot.services.db_commands import get_item
logger = logging.getLogger(__name__)


async def user_start(message: Message):
    await message.reply(f"Йоу :D")
    

async def user_say(message: Message):
    await message.reply(f"Привет, {message.from_user.first_name}!")
    try:          
        sum: int = 0
        mess = message.text
        arr = mess.split('\n')
        answer: str = ""
        for line in arr: 
            sum += eval(line)
            answer += line + " == " + str(eval(line)) + "\n"
        await message.reply(f"{answer} \n Итого: {sum}")
    except Exception as error:
            await message.reply(f"Вводите только арифметические знаки и цифры!")
            logger.error(f'The message about stopping the bot did not go away.'
                         f' Error {error}')

async def eoneguy(message: Message):
    await message.reply("Wait, Eoneguy is still alive???:)")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(eoneguy, user_id=[12345678], text="EOG")
    dp.register_message_handler(user_say, content_types=types.ContentType.ANY, state="*")

# # Хендлер на команду /menu
# @dp.message_handler(Command("menu"))
# async def show_menu(message: types.Message):
#     # Выполним функцию, которая отправит пользователю кнопки с доступными категориями
#     await list_categories(message)


# # Та самая функция, которая отдает категории. Она может принимать как CallbackQuery, так и Message
# # Помимо этого, мы в нее можем отправить и другие параметры - category, subcategory, item_id,
# # Поэтому ловим все остальное в **kwargs
# async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
#     # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)
#     markup = await categories_keyboard()

#     # Проверяем, что за тип апдейта. Если Message - отправляем новое сообщение
#     if isinstance(message, Message):
#         await message.answer("Смотри, что у нас есть", reply_markup=markup)

#     # Если CallbackQuery - изменяем это сообщение
#     elif isinstance(message, CallbackQuery):
#         call = message
#         await call.message.edit_reply_markup(markup)


# # Функция, которая отдает кнопки с подкатегориями, по выбранной пользователем категории
# async def list_subcategories(callback: CallbackQuery, category, **kwargs):
#     markup = await subcategories_keyboard(category)

#     # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
#     await callback.message.edit_reply_markup(markup)


# # Функция, которая отдает кнопки с Названием и ценой товара, по выбранной категории и подкатегории
# async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
#     markup = await items_keyboard(category, subcategory)

#     # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
#     await callback.message.edit_text(text="Смотри, что у нас есть", reply_markup=markup)


# # Функция, которая отдает уже кнопку Купить товар по выбранному товару
# async def show_item(callback: CallbackQuery, category, subcategory, item_id):
#     markup = item_keyboard(category, subcategory, item_id)

#     # Берем запись о нашем товаре из базы данных
#     item = await get_item(item_id)
#     text = f"Купи {item.name}"
#     await callback.message.edit_text(text=text, reply_markup=markup)


# # Функция, которая обрабатывает ВСЕ нажатия на кнопки в этой менюшке
# @dp.callback_query_handler(menu_cd.filter())
# async def navigate(call: CallbackQuery, callback_data: dict):
#     """
#     :param call: Тип объекта CallbackQuery, который прилетает в хендлер
#     :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
#     """

#     # Получаем текущий уровень меню, который запросил пользователь
#     current_level = callback_data.get("level")

#     # Получаем категорию, которую выбрал пользователь (Передается всегда)
#     category = callback_data.get("category")

#     # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
#     subcategory = callback_data.get("subcategory")

#     # Получаем айди товара, который выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
#     item_id = int(callback_data.get("item_id"))

#     # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
#     levels = {
#         "0": list_categories,  # Отдаем категории
#         "1": list_subcategories,  # Отдаем подкатегории
#         "2": list_items,  # Отдаем товары
#         "3": show_item  # Предлагаем купить товар
#     }

#     # Забираем нужную функцию для выбранного уровня
#     current_level_function = levels[current_level]

#     # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
#     await current_level_function(
#         call,
#         category=category,
#         subcategory=subcategory,
#         item_id=item_id
#     )