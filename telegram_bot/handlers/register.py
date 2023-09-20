import json

import httpx
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from keyboards.kb import menu
from .utilits import get_user_api
from config import settings

router = Router()


class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_password = State()
    waiting_for_email = State()
    waiting_for_confirmation = State()


@router.callback_query(F.data == "auth",)
async def register_handler(message: Message, state: FSMContext):
    await message.answer("Давайте начнем регистрацию. Введите ваше имя.")
    await state.set_state(RegistrationStates.waiting_for_name)


@router.message(RegistrationStates.waiting_for_name)
async def valid_name(message: Message, state: FSMContext):
    user = await get_user_api(message.text.lower())
    if user.status_code == 200:
        await message.answer(f"{message.text.lower()}уже занят придумайте другое имя")
    await state.update_data(name=message.text.lower())

@router.message(RegistrationStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):

    await message.answer("Спасибо.Теперь введите ваша почту.")
    await state.set_state(RegistrationStates.waiting_for_email)


@router.message(RegistrationStates.waiting_for_email)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text.lower())
    await message.answer("Спасибо. Теперь введите ваш пароль.")
    await state.set_state(RegistrationStates.waiting_for_password)


@router.message(RegistrationStates.waiting_for_password)
async def process_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    user_data = await state.get_data()

    await message.answer(f"Спасибо.{user_data['name']}, идет регистрация на сервере")


    # Здесь вы можете сформировать JSON-файл на основе данных пользователя
    user_data = {
            "email":  user_data['email'],
            "password": user_data['password'],
            "username": user_data['name']
}
    json_data = json.dumps(user_data)
    api_url = "http://127.0.0.1:8000/auth/register"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(api_url, data=json_data)
            if response.status_code == 201:
                await message.answer("Регистрация успешна!")
            else:
                await message.answer("Ошибка при регистрации.")
        except Exception as e:
            await message.answer(f"Произошла ошибка при регистрации: {str(e)}")