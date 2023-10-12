import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    SECRET_AUTH: str = os.getenv("SECRET_AUTH")


settings = Settings()
