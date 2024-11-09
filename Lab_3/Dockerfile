FROM ubuntu:22.04

RUN apt-get update && apt-get install netcat postgresql-client -y

WORKDIR script/

COPY post_init.sh .
COPY insert_users.sql .
COPY insert_files_and_folders.sql .

RUN chmod +x post_init.sh

CMD ["./post_init.sh"]