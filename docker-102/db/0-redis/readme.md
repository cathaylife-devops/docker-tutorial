# Redis


```bash
# 練習1:
docker pull redis
docker run --name learn-redis -d redis
docker exec -i learn-redis redis-cli ping
docker exec -it `id or name` sh

# 練習2: 轉換為使用 docker-compose
docker-compose up -d
docker exec -i learn-redis redis-cli ping
```
