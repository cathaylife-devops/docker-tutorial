# More container

```bash
#練習三： 指定 `image` 及 `tag` 下載至本機
docker pull debian:buster-slim
docker run --name my-debian --rm -it -v $PWD:/workspace debian:buster-slim

#練習四：使用 nginx 建立 web server，直接進入 container(-it 開啟虛擬終端機，以互動的模式執行)
docker run --name my-nginx -p 8080:80 -it --rm nginx:alpine

#練習五：使用 nginx 建立 web server，背景執行
docker run --name my-nginx -p 8080:80 -d --rm nginx:alpine 
docker exec -it `container-id` sh
```


# Ref:
- https://hub.docker.com/_/nginx
