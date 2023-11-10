import asyncio

from database import create_mongo_connection, insert_data


async def main():
    # Создайте соединение с MongoDB
    client = await create_mongo_connection()

    # Выберите базу данных и коллекцию
    db = client.my_database  # Замените на имя вашей базы данных
    collection = db.my_collection  # Замените на имя вашей коллекции

    # Данные, которые вы хотите добавить в базу данных
    data = {
        "key1": "value1",
        "key2": "value2",
        # Дополнительные поля
    }

    # Вызовите функцию для добавления данных
    success = await insert_data(collection, data)

    if success:
        print("Данные успешно добавлены в базу данных.")
    else:
        print("Произошла ошибка при добавлении данных.")


if __name__ == "__main__":
    asyncio.run(main())
