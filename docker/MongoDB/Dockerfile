FROM mongo:latest

# Копируем скрипт инициализации в контейнер
COPY start.sh /docker-entrypoint-initdb.d/

# Задаем переменные окружения, если необходимо
ENV MONGO_INITDB_ROOT_USERNAME ${MONGO_USER}
ENV MONGO_INITDB_ROOT_PASSWORD ${MONGO_PASSWORD}
ENV MONGO_INITDB_DATABASE ${MONGO_DATABASE}
