from fastapi import FastAPI

from auth.routers import router as users_router
from book_service.routers import router as books_router
from config import settings

app = FastAPI(
    title=settings.app_title,
)

app.include_router(books_router)
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
