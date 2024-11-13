#!/bin/bash

set -x
while ! nc -z db 5432; do
  echo "Ожидаем готовности базы данных..."
  sleep 1
done

while ! nc -z file_service 5001; do
  echo "Ожидаем готовности сервиса..."
  sleep 1
done

echo "Все сервисы готовы."

export PGPASSWORD='qwerty12345'
psql -h db -p 5432 -U username -d file_db -f insert_files_and_folders.sql