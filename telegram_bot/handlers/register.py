import json
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.filters import Command
from .api import get_user_api, post_register_user_api

router = Router()


class RegistrationStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_password = State()
    waiting_for_email = State()
    waiting_for_valid_name = State()


@router.message(Command("auth"))
@router.callback_query(F.data == "auth")
async def register_handler(message: Message, state: FSMContext):
    await message.answer("Давайте начнем регистрацию. Введите ваше имя.")
    await state.set_state(RegistrationStates.waiting_for_valid_name)


@router.message(RegistrationStates.waiting_for_valid_name)
async def valid_name(message: Message, state: FSMContext):
    user = await get_user_api(message.text.lower())
    if user.status_code == 200:
        await message.answer(
            f"Имя'{message.text.lower()}' уже занято, придумайте другое имя"
        )
    elif user.status_code == 404:
        await state.update_data(name=message.text.lower())
        await message.answer("Спасибо. Теперь введите вашу почту.")
        await state.set_state(RegistrationStates.waiting_for_email)

    else:
        await message.answer(
            f"Ошибка на сервере {user.status_code}, попробуйте чуть позже"
        )
        await state.clear()


@router.message(RegistrationStates.waiting_for_email)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text.lower())
    await message.answer("Спасибо. Теперь введите ваш пароль.")
    await state.set_state(RegistrationStates.waiting_for_password)


@router.message(RegistrationStates.waiting_for_password)
async def process_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Спасибо, {user_data['name']}, идет регистрация.")

    user_data = {
        "email": user_data['email'],
        "password": user_data['password'],
        "username": user_data['name']
    }
    json_data = json.dumps(user_data)
    print(json_data)
    response = await post_register_user_api(json_data)
    try:
        if response.status_code == 201:
            await message.answer("Регистрация успешна!")
            await state.clear()
        else:
            await message.answer("Ошибка при регистрации.")
            await state.clear()
    except Exception as e:
        await message.answer(f"Произошла ошибка при регистрации: {str(e)}")
