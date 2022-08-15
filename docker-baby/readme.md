# 簡報

## Hands On Docker

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

練習六： 查看 image 和 container 的記錄

```bash
docker log [container id or name]
```

練習七： 用 hello-world image 起一個 container，再起一個有給指定名稱的 container

```bash
docker run hello-world

docker run --name first hello-world
```

練習八： 刪除 image

```bash
docker rmi hello-world
```

練習九： 批量刪除 container 和 image

```bash
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

## 深入練習

暖身題：請問以下指令是在做哪些事情？

```bash
docker run --detach --publish=80:80 --name=webserver nginx
```

*A: 起一個 nginx container 給他 `80` port 並給他名稱 `webserver`*

html素材：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Docker Workshop</title>
</head>
<body>
  Hello world~!
</body>
</html>
```

練習一： Contianer 裡面的資料和本機的空間是不同的

```bash
//進入 container
docker exec -it [container id or name] bash

pwd
ls

//離開 container
exit
```

練習二：把靜態網頁掛載 nginx container 的 `/usr/share/nginx/html` 能用 `8080` port 開啟網頁

```bash
// 建立html資料夾放靜態網頁
mkdir html
cd html
touch index.html

// 編輯檔案
vi index.html
// 開始 insert
i
// 結束 insert
esc
// 結束編輯檔案
:wq!

// 建立html資料夾放靜態網頁
docker run -d -p=8080:80 -v $PWD/html:/usr/share/nginx/html --name=cathaylife nginx
```

## Ref

- https://hub.docker.com/_/hello-world
