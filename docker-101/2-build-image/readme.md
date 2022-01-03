# Build Image

Goals:

1. build & run
2. push image to [Docker Hub](https://hub.docker.com/)

```bash
# step 1: build & run
docker build -t demo-image:v0.1.0 .
docker run --rm demo-image:v0.1.0

# step 2: push image to Docker Hub
docker tag demo-image:v0.1.0 [username]/demo-image:v0.1.0
docker push [username]/demo-image:v0.1.0
```

## Exercise

### Task 1

1. 建立一版新的 demo-image:v0.2.0，讓 Container 啟動時執行 sl 指令

Checkpoint:

- [ ] 以 demo-image:v0.2.0 啟動一個 Container，確認 sl 指令有正常執行
