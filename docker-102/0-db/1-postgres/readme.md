# postgres

```bash
# 練習1: 建立 postgres db
docker pull postgres:latest
docker run --name learn-postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=rootpwd -d postgres postgres:latest

docker exec -i learn-postgres psql -U root -c "CREATE ROLE \"readonly\" NOINHERIT;"
docker exec -i learn-postgres psql -U root -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO \"readonly\";"
docker exec -i learn-postgres psql -U root -c "SELECT rolname FROM pg_roles;"

# 練習2: 轉換為使用 docker-compose
docker-compose up -d
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' `container_id`
```

## DBeaver

[DBeaver](https://dbeaver.io/) 是一個跨平台的資料庫管理工具，支援 MySQL, PostgreSQL, SQLite, Oracle, DB2, SQL Server, Sybase, MS Access, Teradata, Firebird, Apache Hive, Phoenix, Presto 等資料庫。

用 Container 建立 DB 後可以利用 DBeaver 檢視與管理資料庫。
