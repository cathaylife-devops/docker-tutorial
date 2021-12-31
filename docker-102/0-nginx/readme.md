# Nginx

web server with ningx container

```bash
# 練習1: 建立 nginx web server
docker build -t nginx-demo:v1.0.2 .
docker run -d -p 8080:80 --rm nginx-demo:v1.0.2

# 練習2: 轉換為使用 docker-compose
docker-compose up -d
```
