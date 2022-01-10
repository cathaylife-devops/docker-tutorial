FROM debian:buster-slim

WORKDIR /app

COPY ./hello.txt /app

RUN apt-get update && \
    apt-get -y install sl

CMD cat /app/hello.txt
