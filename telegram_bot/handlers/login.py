import json
from typing import Any
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from .api import fetch_login_cookies

router = Router()


class LoginStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_password = State()


@router.message(Command("login"))
async def get_login(message: Message, state: FSMContext):
    await message.answer(" Введите ваше имя.")
    await state.set_state(LoginStates.waiting_for_name)


@router.message(LoginStates.waiting_for_name)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(name=message.text.lower())
    await message.answer("Спасибо. Теперь введите ваш пароль.")
    await state.set_state(LoginStates.waiting_for_password)


@router.message(LoginStates.waiting_for_password)
async def process_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Спасибо, {user_data['name']}, вход.")

    user_data = {
        "password": user_data['password'],
        "username": user_data['name']
    }
    json_data = json.dumps(user_data)
    print(json_data)
    response = await fetch_login_cookies(json_data)
    print(response)
