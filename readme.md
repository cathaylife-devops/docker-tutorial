# Docker Tutorial

## Goals

1. 了解 Docker/Container 的基礎知識
2. 基礎 Command 操作
3. Dockerfile 撰寫
4. docker-compose 撰寫與使用
5. 使用情境

## Requiremens

安裝 Docker, docker-compose

1. Mac / Windows  
    安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Linux
    安裝 Docker Engine，[Debian](https://docs.docker.com/engine/install/debian/)、[Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    安裝 [docker-compose](https://docs.docker.com/compose/install/#install-compose)

執行以下指令，確認 Docker 可以正常運作

```bash
docker run -d -p 80:80 docker/getting-started
```

## Reference

1. [Docker Docs - Get Started](https://docs.docker.com/get-started/)
