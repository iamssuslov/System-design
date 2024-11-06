#!/bin/bash

set -x

while ! nc -z db 5432; do
  echo "Ожидаем запуска базы данных..."
  sleep 1
done

python3 start_script.py
python3 app.py