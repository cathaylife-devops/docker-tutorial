# Multi Stage Build

```bash
docker build -t spring-boot-app:0.1.0 .
docker run --rm -p 8080:8080 spring-boot-app:0.1.0
```

## Ref

1. [Docker doc - Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)
2. [Spring Boot Example](https://github.com/spring-guides/gs-spring-boot)
