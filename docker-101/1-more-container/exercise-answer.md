# Exercise Answer

## Task 1

使用 nginxdemos:hello 建立一個名稱為 task-nginx，且為 Daemon 模式的 Container，並將 Host 的 8888 port 對應至 Container 的 80 port

Check point:

- [x] 確認 localhost:8888 有出現 nginx hello 頁面
- [x] 檢視新生成的 Container 名稱為 ```task-nginx```
- [x] Terminal 完全關閉後，Container 仍正常執行，確認 Container 是以 Daemon mode 執行
- [x] 刪除 task-nginx container

```bash
docker run --name task-nginx -d -p 8888:80 nginxdemos:hello
# Open a browser and go to localhost:8888

# check container name
docker ps 

# remove task-nginx container
docker stop task-nginx
docker rm task-nginx
# or
docker rm -f task-nginx
```

## Task 2

1. 使用 debian:buster-slim 建立一個名稱為 sl-debian 且執行結束後會自動刪除的 Container，並直接進入 Container
2. 安裝 sl package，安裝指令為 ```apt-get update && apt-get install sl```
3. 執行 sl
4. 離開 Container 時讓 Container 自動刪除

Check point:

- [x] sl 可正常執行
- [x] 離開 Container 後，查詢所有狀態的 Container，確定名稱為 sl-debian 的 Container 已經不存在

```bash
docker run -it --rm --name sl-debian debian:buster-slim
# in container
apt-get update && apt-get install sl
sl
exit
```

## Task 3

1. 撰寫一份 index.html
2. 使用 nginx:alpine 建立一個名稱為 web-server 的 Container
3. index.html 所在的目錄掛載至 nginx container 的 ```/usr/share/nginx/html``` 中
4. 將 Host 的 80 port 對應至 Container 的 80 port

- [x] 確認 localhost 有出現 index.html 的內容

```bash
mkdir html
echo "Hello Stranger" >> html/index.html
docker run --name web-server -p 80:80 -v $PWD/html:/usr/share/nginx/html nginx:alpine
# Open a browser and go to localhost
```
