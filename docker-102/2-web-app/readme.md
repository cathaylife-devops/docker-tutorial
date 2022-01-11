# Web Applicaiton

1. Web App - [FastAPI](https://fastapi.tiangolo.com/) Python API framework
2. DB - [Redis](https://redis.io/) In-Memory DB

使用 Docker Compose 建立 Web App 與 DB 的 Container，並讓 Web App 連接 DB

```bash
docker exec -i `container id or name` redis-cli get 'count'
```

## Ref

- https://docs.docker.com/compose/gettingstarted/
