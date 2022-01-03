# Nexus

[Nexus Repository OSS](https://www.sonatype.com/products/repository-oss) 是 Nexus Repository 的開源版本，可以管理各式 Artifact，並內建各種 Repository，如: Maven、Pypi、npm 等，其中 nexus3 更是支援 Docker registry。

Nexus 提供 bare-metal 安裝與 Docker Image，透過官方提供的 Compose file 可以快速建立一個 Nexus。

預設 Admin 帳號密碼：

- 帳號：admin
- 密碼：可以在 Nexus 啟動後位於 ```/nexus-data``` 目錄中的 ```admin.password``` 的檔案中找到，[Nexus Docs](https://github.com/sonatype/docker-nexus3#notes)

```bash
# 啟動 nexus3
docker-compose up -d
# 會看到一個由 docker compose 自行建立的 volume，名稱為 `xxx_nexus-data`
docker volume ls
# 查看 log
docker-compose logs
# 查詢第一次登入的管理者密碼
docker exec -i {container_id} cat /nexus-data/admin.password &&  echo ''
```

## Ref

1. [docker-nexus3]https://github.com/sonatype/docker-nexus3
