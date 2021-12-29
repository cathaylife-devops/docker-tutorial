# Run container

```bash
#練習一： 會先確認本機是否有下載過 `hello-world`，沒有的話會自動下載 latest 版本 image
docker run hello-world

#練習二： 指定 `image` 及 `tag` 下載至本機
docker pull debian:buster-slim
docker run --rm -it -v $PWD:/workspace debian:buster-slim
```


# Ref:
- https://hub.docker.com/_/hello-world
- https://hub.docker.com/_/debian
