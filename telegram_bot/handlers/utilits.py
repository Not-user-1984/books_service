import httpx


async def get_user_api(username: str):
    user = f"http://127.0.0.1:8000/users/{username}"
    async with httpx.AsyncClient() as client:
            return  await client.get(user)
