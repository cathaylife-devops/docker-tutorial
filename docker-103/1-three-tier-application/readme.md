# Three Tier Application

1. frontend: Nginx web server
2. backend: FastAPI Application
3. database:
   1. PostgreSQL
   2. pgAdmin4

frontend, backend, db 因為都在同一個 docker compose 中，預設會被加入同一個 network 中，因此彼此可以用 compose 中的 service 名稱作為 hostname 溝通，如目前這份 compose 中的 ```services```、```backend```、```frontend```。

## Build

```bash
docker-compose build
```

## Run

若 Image 還沒有 build 過會先 build 再啟動

```bash
docker-compose up -d
```

Index: [localhost](http://localhost)  
Swagger UI: [localhost/docs](http://localhost/docs)  
ReDoc: [localhost/redoc](http://localhost/redoc)  
OpenAPI Spec: [localhost/openapi.json](http://localhost/openapi.json)  
