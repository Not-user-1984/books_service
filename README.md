# FastAPI service bookshop


Находиться в стадии разработки, есть начальный репозиторий, 
[Bookstore_Program](https://github.com/Not-user-1984/Bookstore_Program)

### Запуск
``` cmd
cd infra
развернуть базу данных через докер
docker compose up -d --build
залить по желанию свои данные в .env

установить витруалку и все зависимости

запуск FastAPI
cd src
uvicorn main:app --reload

дока тут:

http://127.0.0.1:8000/docs/

```

- [x] Подключение базы, миграции и urls.
- [ ] grud проекта(асинхронно, пока создание Book не работает)




