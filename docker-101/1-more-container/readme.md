# More container

## Command

覆寫 Container 在 Image 中被設定的 Command，執行其他 Command

``` bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

練習一：使用 busybox image，簡單操作 ping 指令

```bash
docker run busybox ping -c 3 google.com
```

## docker run

[Docker docs](https://docs.docker.com/engine/reference/commandline/run/)

練習二：指定 `image` 及 `tag` 下載至本機

```bash
docker pull debian:buster-slim
```

### --rm

Container 執行完畢後自動刪除

練習三：執行完畢後，Container 被自動刪除

```bash
docker run --rm busybox ping -c 3 google.com
docker ps -a
```

### --name

指定 Container 的名稱

練習四：指定 Container name

```bash
docker run --name my-debian debian:buster-slim
docker ps -a
```

### -it

-i: --interactive，互動模式
-t: --tty，配置一個虛擬的終端機

效果類似於 SSH 連線進入 Container 中操作

練習五：以 -it 進入 Container 中

```bash
docker run -it --rm debian:buster-slim
```

### -v

掛載本機目錄至 Container 中，本機目錄須以絕對路徑表示，```$PWD``` 為當前目錄完整路徑的環境變數，掛載的目錄稱之為 ```Volume```

非儲存在 Volume 中的檔案在 Container 關閉後都會被移除。若有資料需要保存，務必儲存於 Volume 中。Host 與 Container 可共同讀取的目錄只有 Volume。

```-v [本機目錄]:[Container 目錄]```

練習六：掛載指定目錄至 Container 中

```bash
docker run --rm -v $PWD:/workspace -it debian:buster-slim
```

因為 ```-it``` 所以已經進入 Container 的 Terminal，執行以下指令

```bash
ls -lha /
ls -lha /workspace
```

### -p

Host 與 Container Port 的映射，常用於

```-p [host port]:[container port]```

練習七：將 Host 的 8080 port 映射至 Container 的 80 port

```bash
docker run --rm --name my-nginx -p 8080:80 nginx:alpine
```

前往 [localhost:8080](localhost:8080) 驗證結果

### -d

以 [Daemon](https://zh.wikipedia.org/wiki/%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B) 守護行程方式啟動 Container，等同於背景執行，不會受當前終端機關閉影響

練習八：使用 nginx 建立 web server，背景執行

```bash
docker run --name my-nginx -p 8080:80 -d --rm nginx:alpine 
```

前往 [localhost:8080](localhost:8080) 驗證結果

## docker logs

查看 Container 的 Log

[Docker docs](https://docs.docker.com/engine/reference/commandline/logs/)

練習九：查閱 Container Log

```bash
docker run --name my-nginx -p 8080:80 -d --rm nginx:alpine 
docker logs my-nginx
```

```--tail``` 或 ```-n``` 參數指定印出最後 10 行 log

```bash 
docker logs --tail 10 my-nginx
docker logs -n 10 my-nginx
```

以跟隨模式監看 log

```bash
docker logs -f my-nginx
docker logs -n 10 -f my-nginx
```

## docker cp

如前面 Volume 掛載所述，Host 與 Container 可共同讀取的目錄只有 Volume。若在 Container 建立時就沒有掛載 Volume，則無法再另外掛載。這時若想要在 Host 與 Container 進行檔案交換可以使用 ```docker cp``` 指令。

```bash
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
docker cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH
```

[Docker docs](https://docs.docker.com/engine/reference/commandline/cp/)

練習十：Host 與 Container 檔案交換

```bash
docker run --name my-debian -it --rm debian:buster-slim
```

因為 ```-it``` 所以已經進入 Container 的 Terminal，執行以下指令，驗證 Container 中有 os-release 這個檔案

```bash
cat /etc/os-release
```

開啟另一個 Terminal，將 my-debian 的 /etc/os-release 複製至當前目錄

```
docker cp my-debian:/etc/os-release ./
```

## docker exec

當 Container 已經在執行中時，可以透過 ```docker exec``` 在 Container 執行特定指令

練習十一：在執行中的 Container 執行其他指令，以及進入 Container 中

```bash
docker run --name my-nginx -p 8080:80 -d --rm nginx:alpine 
docker exec my-nginx cat /etc/os-release
docker exec -it my-nginx /bin/sh
```

因為 ```-it``` 所以已經進入 Container 的 Terminal，執行以下指令

```bash
cat /etc/os-release
```

## FAQ

1. 執行 ```docker rm [container name / id]``` 時出現以下錯誤
    ```txt
    Error response from daemon: You cannot remove a running container 56ab97a2cd087bffd0188cd03374c1d4a034e8ba43672f9f7d99fb4a615b535e. Stop the container before attempting removal or force remove
    ```
    - 原因

        因為要刪除的 Container 仍在執行中，所以無法刪除該 Container
    
    - 解決方法

        先停止 Container，再進行刪除

        ```bash
        docker stop [container name / id]
        docker rm [container name / id]
        ```

        或者增加 ```-f``` option，以強制模式刪除 Container

        ```bash
        docker rm -f [container name / id]
        ```

2. 執行 ```docker rmi [image name / id]``` 時出現以下錯誤

    ```txt
    Error response from daemon: conflict: unable to remove repository reference "debian:buster-slim" (must force) - container 56ab97a2cd08 is using its referenced image e659ceeeff6c
    ```

    - 原因

        因為有 Container 正在使用要刪除的 Image，所以無法刪除該 Image 

    - 解決方法

        先刪除使用該 Image 的 Container 後再刪除 Image

        ```bash
        docker stop [container name / id]
        docker rm [container name / id]
        docker rmi [image name / id]
        ```

3. 以 ```-it``` 搭配 ```bash``` 或 ```sh``` 進入 Container 後如何離開？

    按下 Ctrl + D 或是輸入 ```exit```

4. 未使用 Daemon 模式啟動 Container 時如何停止？

    按下 Ctrl + C

5. Container 佔用的硬碟空間大小為何？

    ```bash
    docker ps -as
    ```

6. Container、Image 使用的硬碟空間目錄在哪？

    執行 ```docker info``` 指令可以顯示 Docker 的相關資訊，```Docker Root Dir``` 的值即為 Docker 儲存所有資料的位置，若沒有另外設定通常值為 ```/var/lib/docker```。

    Mac 或 Windows 使用 Docker Desktop 時，一般都是由 Docker Desktop 啟動 Linux 虛擬機執行，所以執行 ```docker info``` 時仍會發現 ```Docker Root Dir``` 也是 ```/var/lib/docker```。若安裝時皆使用預設值，實際對應在本機的位置如下：

    - Windows: C:\ProgramData\DockerDesktop
    - MacOS: ~/Library/Containers/com.docker.docker/Data/vms/0/

    [Docker Docs](https://docs.docker.com/engine/reference/commandline/info/)

## Exercise

### Task 1

使用 nginxdemos:hello 建立一個名稱為 task-nginx，且為 Daemon 模式的 Container，並將 Host 的 8888 port 對應至 Container 的 80 port

Check point:

- [ ] 確認 localhost:8888 有出現 nginx hello 頁面
- [ ] 檢視新生成的 Container 名稱為 ```task-nginx```
- [ ] Terminal 完全關閉後，Container 仍正常執行，確認 Container 是以 Daemon mode 執行
- [ ] 刪除 task-nginx container

### Task 2

1. 使用 debian:buster-slim 建立一個名稱為 sl-debian 且執行結束後會自動刪除的 Container，並直接進入 Container
2. 安裝 sl package，安裝指令為 ```apt-get update && apt-get install sl```
3. 執行 sl
4. 離開 Container 時讓 Container 自動刪除

Check point:

- [ ] sl 可正常執行
- [ ] 離開 Container 後，查詢所有狀態的 Container，確定名稱為 sl-debian 的 Container 已經不存在

### Task 3

1. 撰寫一份 index.html
2. 使用 nginx:alpine 建立一個名稱為 web-server 的 Container
3. index.html 所在的目錄掛載至 nginx container 的 ```/usr/share/nginx/html``` 中
4. 將 Host 的 80 port 對應至 Container 的 80 port

- [ ] 確認 localhost 有出現 index.html 的內容

## Ref

- https://hub.docker.com/_/nginx
- [What is tty?](https://flykof.pixnet.net/blog/post/24277709)
