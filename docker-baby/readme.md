# 簡報

## Hands On Docker

[Docker Hub](https://hub.docker.com/)  
[Docker playground](https://labs.play-with-docker.com/)

> 打開 playground 點選 `ADD NEW INSTANCE`

練習一： 假設自己在家裡安裝Docker，可以透過 ```docker info``` 確認所有 docker 的資訊( conatiner,image,network,cgroup,cpu...)

```bash
docker info
```

練習二： 看看本機有哪些 Docker Image、Container

```bash
docker images

docker ps -a
docker ps
```

練習三： 拉一個 hello-world image

```bash
docker pull hello-world
```

練習四： 用 hello-world image 建立一個 container，再建立一個有指定名稱的 container，再分別起 container

```bash
docker create hello-world
docker create --name first hello-world

docker start
docker start -i [container id or name]
```

練習五： 刪除 container

```bash
docker rm [container id or name]
```

練習六： 用 hello-world image 起一個 container，再起一個有給指定名稱的 container

```bash
docker run hello-world

docker run --name first hello-world
```

練習七： 刪除 image

```bash
docker rmi hello-world
```

練習九： 批量刪除 container 和 image

```bash
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

## 深入練習

練習題：起一個 nginx container 給他 `80` port 並給他名稱 `webserver`

```bash
docker run --detach --publish=80:80 --name=webserver nginx
```

## Ref

- https://hub.docker.com/_/hello-world
