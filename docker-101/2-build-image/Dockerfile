FROM debian:buster-slim

WORKDIR /app

COPY ./hello.txt /app

RUN apt-get update && \
    apt-get install -y sl

CMD cat /app/hello.txt
