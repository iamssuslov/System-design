FROM python:3.11-slim

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3-pip netcat

WORKDIR file_service/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

RUN chmod +x run.sh

CMD ["./run.sh"]
