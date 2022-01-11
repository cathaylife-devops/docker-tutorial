# Redis

練習1:

```bash
docker pull redis
docker run --name learn-redis -d redis
docker exec -i learn-redis redis-cli ping
docker rm -f learn-redis
```

練習2: 轉換為使用 docker-compose

```bash
docker-compose up -d
docker exec -i learn-redis redis-cli ping
docker-compose down
```
