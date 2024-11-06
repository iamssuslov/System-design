#!/bin/bash
set -x

echo "=== Начало инициализации базы данных ==="
psql -v ON_ERROR_STOP=1 --username="$POSTGRES_USER" <<-EOSQL
    CREATE USER username WITH PASSWORD 'qwerty12345';


    CREATE DATABASE user_db;
    GRANT ALL PRIVILEGES ON DATABASE user_db TO username;

    \connect user_db;
    ALTER SCHEMA public OWNER TO username;
    GRANT ALL ON SCHEMA public TO username;

    CREATE DATABASE file_db;
    GRANT ALL PRIVILEGES ON DATABASE file_db TO username;

    \connect file_db;
    ALTER SCHEMA public OWNER TO username;
    GRANT ALL ON SCHEMA public TO username;
EOSQL
echo "=== Инициализация базы данных завершена ==="
