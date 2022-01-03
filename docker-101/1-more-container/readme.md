# More container

## Command

覆寫 Container 在 Image 中被設定的 Command，執行其他 Command

``` bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

```bash
#練習一： 使用 busybox image，簡單操作 ping 指令
docker run busybox ping -c 3 google.com
```

## docker run

[Docker docs](https://docs.docker.com/engine/reference/commandline/run/)

```bash
#練習二： 指定 `image` 及 `tag` 下載至本機
docker pull debian:buster-slim
```

### --rm

Container 執行完畢後自動刪除

```bash
#練習三： 執行完畢後，Container 被自動刪除
docker run --rm busybox ping -c 3 google.com
docker ps -a
```

### --name

指定 Container 的名稱

```bash
#練習四： 指定 Container name
docker run --name my-debian debian:buster-slim
docker ps -a
```

### -it

-i: --interactive，互動模式
-t: --tty，配置一個虛擬的終端機

效果類似於 SSH 連線進入 Container 中操作

```bash
#練習五： 以 -it 進入 Container 中
docker run -it --rm debian:buster-slim
```

### -v

掛載本機目錄至 Container 中，本機目錄須以絕對路徑表示，```$PWD``` 為當前目錄完整路徑的環境變數，掛載的目錄稱之為 ```Volume```

非儲存在 Volume 中的檔案在 Container 關閉後都會被移除。若有資料需要保存，務必儲存於 Volume 中。Host 與 Container 可共同讀取的目錄只有 Volume。

```-v [本機目錄]:[Container 目錄]```

```bash
#練習六： 掛載指定目錄至 Container 中
docker run --rm -v $PWD:/workspace -it debian:buster-slim
# In container
ls -lha /
ls -lha /workspace
```

### -p

Host 與 Container Port 的映射，常用於

```-p [host port]:[container port]```

```bash
#練習七： 將 Host 的 8080 port 映射至 Container 的 80 port
docker run --rm --name my-nginx -p 8080:80 nginx:alpine
# Open a browser and go to localhost:8080
```

### -d

以 [Daemon](https://zh.wikipedia.org/wiki/%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B) 守護行程方式啟動 Container，等同於背景執行，不會受當前終端機關閉影響

```bash
#練習八：使用 nginx 建立 web server，背景執行
docker run --name my-nginx -p 8080:80 -d --rm nginx:alpine 
# Open a browser and go to localhost:8080
docker exec -it `container-id` sh
```

## docker logs

查看 Container 的 Log

[Docker docs](https://docs.docker.com/engine/reference/commandline/logs/)

```bash
#練習九：查閱 Container Log
docker run --name my-nginx -p 8080:80 -d --rm nginx:alpine 
# 印出所有 log
docker logs my-nginx
# 印出最後 10 行 log
docker logs --tail 10 my-nginx
docker logs -n 10 my-nginx
# 以跟隨模式監看 log
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

```bash
#練習十：Host 與 Container 檔案交換
docker run --name my-debian -it --rm debian:buster-slim
# in container my-debian
cd /tmp
echo "Hi, host" >> hello.txt
cat hello.txt
# another terminal in host
docker cp my-debian:/tmp/hello.txt ./
cat hello.txt
echo "Hi, my-debian" >> hello.txt
docker cp hello.txt my-debian:/tmp/hello.txt
# in container my-debian
cd /tmp
cat hello.txt
```

## Exercise

### Task 1

使用 nginxdemos:hello 建立一個名稱為 task-nginx，且為 Daemon 模式的 Container，並將 Host 的 8888 port 對應至 Container 的 80 port

Check point:

- [ ] 確認 localhost:8888 有出現 nginx hello 頁面
- [ ] 檢視新生成的 Container 名稱為 ```task-nginx```
- [ ] Terminal 完全關閉後，Container 仍正常執行，確認 Container 是以 Daemon mode 執行
- [ ] 刪除 task-nginx container

### Task 2

1. 使用 debian:buster-slim 建立一個名稱為 sl-debian 的 Container，並直接進入 Container
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
