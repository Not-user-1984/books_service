import httpx
import json


async def get_user_api(username: str):
    user = f"http://127.0.0.1:8000/users/{username}"
    async with httpx.AsyncClient() as client:
            return await client.get(user)


async def post_register_user_api(data: json):
    api_url = "http://127.0.0.1:8000/auth/register"
    async with httpx.AsyncClient() as client:
            return await client.post(
                api_url,
                data=data)


async def fetch_login_cookies(username, password):
    async with httpx.AsyncClient() as client:
        url = "http://127.0.0.1:8000/auth/jwt/login"
        data = {
            "username": username,
            "password": password,
            "grant_type": "",
            "scope": "",
            "client_id": "",
            "client_secret": ""
        }
        response = await client.post(url, data=data)
        if response.status_code == 204:
            cookies = response.cookies
            return cookies
        else:
            return None
