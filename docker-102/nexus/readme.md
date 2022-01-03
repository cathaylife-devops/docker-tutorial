# Nexus

[Nexus Repository OSS](https://www.sonatype.com/products/repository-oss) 是 Nexus Repository 的開源版本，可以管理各式 Artifact，並內建各種 Repository如 Maven、Pypi、npm、Docker registry 等。

Nexus 提供 bare-metal 安裝與 Docker Image，透過官方提供的 Compose file 可以快速建立一個 Nexus。

預設 Admin 帳號密碼：

帳號：admin
密碼：可以在 Nexus 啟動後位於 ```$data-dir``` 目錄中的 ```admin.password``` 的檔案中找到，[Nexus Docs](https://help.sonatype.com/repomanager3/nexus-repository-administration/access-control/users)

## Ref

1. [docker-nexus]https://github.com/sonatype/docker-nexus
