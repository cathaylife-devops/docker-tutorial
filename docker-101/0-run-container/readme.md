# Run container

```bash
#練習一： 會先確認本機是否有下載過 `hello-world`，沒有的話會自動下載 latest 版本 image
docker run hello-world

#練習二： 看看本機有哪些 Docker Image
docker images

#練習三： 看看本機有哪些 Container
docker ps -a

#練習四： 刪除 Container 
docker rm [container id or name]

#練習五： 刪除 Image
docker rmi hello-world
```

## Ref

- https://hub.docker.com/_/hello-world
