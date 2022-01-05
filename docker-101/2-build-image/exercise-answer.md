# Exercise

## Task 1

1. 建立一版新的 demo-image:v0.2.0，讓 Container 啟動時執行 sl 指令

Checkpoint:

- [x] 以 demo-image:v0.2.0 啟動一個 Container，確認 sl 指令有正常執行

```Dockerfile
FROM debian:buster-slim

WORKDIR /app

COPY ./hello.txt /app

RUN apt-get update && \
    apt-get install sl

CMD sl
```

```bash
docker build -t demo-image:v0.2.0 .
# check demo-image:v0.2.0 image
docker images
docker run --rm demo-image:v0.2.0
```
