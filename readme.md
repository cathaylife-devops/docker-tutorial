# Docker Tutorial

## Goals

1. 了解 Docker/Container 的基礎知識
2. 基礎 Command 操作
3. Dockerfile 撰寫
4. docker-compose 撰寫與使用
5. 使用情境

## Requirements

安裝 Docker, docker-compose

1. Mac / Windows  
    安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Linux
    安裝 Docker Engine，[Debian](https://docs.docker.com/engine/install/debian/)、[Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    安裝 [docker-compose](https://docs.docker.com/compose/install/#install-compose)
3. [GCP Cloud Shell](https://shell.cloud.google.com/)，進入後即可以使用一個具有安裝好 Docker 並配有 VSCode 的虛擬機環境。GCP Cloud Shell 為免費服務無需支費任何費用，每週可使用 50 小時，其他使用限制請參考 [Cloud Shell Doc - Limitations and restrictions](https://cloud.google.com/shell/docs/limitations)。

執行以下指令，確認 Docker 可以正常運作

```bash
docker run -d -p 80:80 docker/getting-started
```

## busybox, alpine, scratch

> busybox: 是一個 Linux 指令工具包，被譽為 Linux 的瑞士刀（如 cat、echo、grep、mount、telnet 等）

> alpine: 以 musl libc(C的標準函式庫，主要用於Linux核心) 及 busybox 為基礎，僅 5 MB 大小的映像檔，適合當做 Base Image 使用

> scratch: 是空的 image(docker 保留字)

## Recommended Resources

1. [Docker Best Practices](https://gist.github.com/luismts/725fd70c7e963884b3a430e55ffb3432)
2. [Container Training](https://github.com/jpetazzo/container.training)

## Reference

1. [Docker Docs - Get Started](https://docs.docker.com/get-started/)
2. [The best Docker base image for your Python application (August 2021)](https://pythonspeed.com/articles/base-image-python-docker-images/)
