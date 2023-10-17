import motor.motor_asyncio

from config import settings


async def connect_to_mongodb():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL_DB)
        db = client[settings.MONGO_DATABASE]
        print("Подключено к MongoDB асинхронно")
        # Теперь вы можете взаимодействовать с базой данных асинхронно
        # например, получить коллекцию
        # collection = db["имя_коллекции"]
    except Exception as e:
        print("Ошибка подключения к MongoDB:", e)


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect_to_mongodb())
