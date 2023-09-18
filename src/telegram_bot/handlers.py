from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import httpx

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("get_data"))
async def get_data_handler(message: Message):
    # URL вашего FastAPI API
    api_url = "http://127.0.0.1:8000/user_books?user_id=10"  # Замените на фактический URL вашего API
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url)
            if response.status_code == 200:
                data = response.json()
                await message.answer(f"Получены данные из API: {data}")
            else:
                await message.answer(f"Ошибка при запросе к API: {response.status_code}")
        except Exception as e:
            await message.answer(f"Произошла ошибка при запросе к API: {str(e)}")


# @dp.message_handler(commands=["register"])
# async def register_user(message: types.Message):
#     user = message.from_user
#     async with SessionLocal() as db_session:
#         db_user = db_session.query(User).filter(User.user_id == user.id).first()
#         if not db_user:
#             db_user = User(
#                 user_id=user.id,
#                 username=user.username,
#               git   full_name=user.full_name
#             )
#             db_session.add(db_user)
#             db_session.commit()
#             await message.answer("Вы успешно зарегистрированы!")
#         else:
#             await message.answer("Вы уже зарегистрированы!")