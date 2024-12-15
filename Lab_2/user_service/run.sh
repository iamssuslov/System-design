#!/bin/bash

set -x

while ! nc -z mongo-db 27017; do
  echo "Ожидаем запуска базы данных..."
  sleep 1
done

while ! nc -z kafka 9092; do
  echo "Ожидаем запуска Kafka..."
  sleep 1
done

python3 start_script.py
python3 app.py