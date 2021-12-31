# Run container

```bash
#練習一： 會先確認本機是否有下載過 `hello-world`，沒有的話會自動下載 latest 版本 image
docker run hello-world

#練習二： 使用 busybox image，簡單操作 ping 指令
docker run busybox ping -c 3 google.com
```


# Ref:
- https://hub.docker.com/_/hello-world
- https://hub.docker.com/_/debian
