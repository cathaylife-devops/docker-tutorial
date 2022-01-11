# postgres

練習1: 建立 postgres db

```bash
docker pull postgres:latest
docker run --name learn-postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=rootpwd -d postgres postgres:latest

docker exec -i learn-postgres psql -U root -c "CREATE ROLE \"readonly\" NOINHERIT;"
docker exec -i learn-postgres psql -U root -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO \"readonly\";"
docker exec -i learn-postgres psql -U root -c "SELECT rolname FROM pg_roles;"
```

練習2: 轉換為使用 docker-compose

```bash
docker-compose up -d
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' `container_id`
```
