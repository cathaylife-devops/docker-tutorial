# Entrypoint

```bash
# 讓 Command 作為 Entrypoint 的參數
docker build -t entrypoint-demo:v1 -f Dockerfile.one .
# Dockerfile.one 與 hi.sh 搭配的寫法讓預設的 Command 作為參數帶入
docker run --rm entrypoint-demo:v1
# # Dockerfile.one 與 hi.sh 搭配的寫法讓覆寫的 Command 作為參數帶入
docker run --rm entrypoint-demo:v1 Cathay

# 使用 Entrypoint 做為初始化功能，執行完畢後才執行 Command
docker build -t entrypoint-demo:v2 -f Dockerfile.two .
docker run --rm entrypoint-demo:v2 
# entrypoint.sh 的寫法讓 Command 能繼續執行其他指令
docker run --rm entrypoint-demo:v2 echo hi
# Override ENTRYPOINT
docker run --rm -it --entrypoint /bin/sh entrypoint-demo:v2
```

## Ref

1. [Dockerfile 中的 ENTRYPOINT](https://medium.com/@xyz030206/dockerfile-%E4%B8%AD%E7%9A%84-entrypoint-9653c3b2d2f8)
