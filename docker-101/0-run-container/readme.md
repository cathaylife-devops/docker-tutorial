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

刪除 Container 時，如果該 Container 仍處於執行中狀態會出現錯誤訊息，提示無法刪除正式在執行中的 Container。可以先下 ```docker stop [container id or name]``` 指令停止再進行刪除，或者加入 ```-f``` 參數強制刪除 ```docker rm -f [container id or name]```。

刪除 Image 時，如果還有 Container 使用該 Image 會出現錯誤訊息，提示有哪個 Container 正在使用該 Image。

## Ref

- https://hub.docker.com/_/hello-world
