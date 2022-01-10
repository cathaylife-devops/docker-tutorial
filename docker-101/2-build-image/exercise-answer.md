# Exercise

## Task 1

1. 建立一版新的 demo-image:v0.2.0，讓 Container 啟動時以 ```/usr/games/sl``` 執行 sl 指令，並使用 ```-t``` 參數配置一個虛擬終端機

Checkpoint:

- [x] 以 demo-image:v0.2.0 啟動一個 Container，確認 sl 指令有正常執行

```Dockerfile
FROM debian:buster-slim

WORKDIR /app

COPY ./hello.txt /app

RUN apt-get update && \
    apt-get -y install sl

CMD /usr/games/sl
```

```bash
docker build -t demo-image:v0.2.0 .
# check demo-image:v0.2.0 image
docker images
docker run --rm -t demo-image:v0.2.0
```
