# Nginx

web server with nginx container

練習1: 建立 nginx web server

```bash
docker build -t nginx-demo:v1.0.2 .
docker run -d -p 8080:80 --rm nginx-demo:v1.0.2
```

練習2: 轉換為使用 docker-compose

```bash
docker-compose up -d
```
