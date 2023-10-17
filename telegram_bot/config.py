import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    SECRET_AUTH: str = os.getenv("SECRET_AUTH")
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")
    MONGO_URL_DB: str = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017/{MONGO_DATABASE}"


settings = Settings()
