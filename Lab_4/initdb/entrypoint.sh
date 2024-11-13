#!/bin/bash

# Файл с данными в формате JSON
DATA_FILE="/docker-entrypoint-initdb.d/data.json"

# Параметры подключения
DB_NAME="users_db"
COLLECTION_NAME="user"
HOST="localhost"
PORT="27017"

# Команда для импорта данных
mongoimport --db $DB_NAME --collection $COLLECTION_NAME --host $HOST --port $PORT --file $DATA_FILE --jsonArray
