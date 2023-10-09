from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply("Hello, admin!")
    sum: int = 0
    arr = message.text
    arr1 = arr.split('\n')
    for line in arr1: 
        sum += eval(line)
    await message.reply(f"Итого: {sum}")
    

async def admin_echo(message: Message):
    await message.reply("HAYo Gitler")
    

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, content_types=types.ContentType.ANY, state="*", is_admin=True)
    #прописываем условия для вызова данной функ           ^              ^              ^
