import httpx
from keyboards import kb
import text
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "get_data")
async def get_data_handler(message: Message):
    # URL вашего FastAPI API
    api_url = "http://127.0.0.1:8000/user_books?user_id=10"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url)
            if response.status_code == 200:
                data = response.json()
                await message.answer(f"Получены данные из API: {data}",)
            else:
                await message.answer(
                    f"Ошибка при запросе к API: {response.status_code}"
                    )
        except Exception as e:
            await message.answer(f"Произошла ошибка при запросе к API: {str(e)}")
