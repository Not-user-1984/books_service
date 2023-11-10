import motor.motor_asyncio


MONGO_URL_DB = "mongodb://user:699699@localhost:27017"


# Функция для установления асинхронного соединения с MongoDB
async def create_mongo_connection():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL_DB)
    return client


# Функция для добавления данных в коллекцию
async def insert_data(collection, data):
    try:
        await collection.insert_one(data)
        return True
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        return False
