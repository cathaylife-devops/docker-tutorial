# Selenium end-to-end testing

[Selenium](https://www.selenium.dev/) 常用於網頁自動化測試與網路爬蟲，可執行預先設定好的腳本，實際開啟瀏覽器與網頁互動，支援多種 OS 與瀏覽器。

想要平行進行大量測試時可以使用 [Selenium Grid](https://www.selenium.dev/documentation/grid/) 搭建一組 Selenium Cluster，由 Hub 統一派發任務給空閒的 Node，藉此優化資源使用率。

Selenium 官方提供了 Selenium Grid Server 的 Docker Image，[Github Repository](https://github.com/SeleniumHQ/docker-selenium)、[Docker Hub](https://hub.docker.com/u/selenium)。

Image 主要有兩種類型：

1. Standalone: 單一個 Image 包含了 Hub 與一個指定瀏覽器的 Node
2. Hub and Nodes: Hub 與 None 分別為獨立的 Image，需設定 Container 環境變數將 Node 註冊至 Hub

Standalone 與 Node Image 都安裝了 [x11vnc](https://github.com/LibVNC/x11vnc) 作為 [VNC](https://zh.wikipedia.org/wiki/VNC) Server，可以使用 [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) 遠端進入 Node 的 Container 中確認瀏覽器的操作畫面，連線預設密碼為 ```secret```。

在 [https://hub.docker.com/u/selenium](https://hub.docker.com/u/selenium) 中都只有建置 AMD64 架構的 Image，如果使用 ARM 架構的 CPU（如 Apple M1），Node 在啟動瀏覽器時會發生瀏覽器 Crashed。因此有另外一個專門為 ARM 架構建置 Image 的 Project [https://github.com/seleniarm/docker-selenium](https://github.com/seleniarm/docker-selenium)，Docker Hub 為 [https://hub.docker.com/u/seleniarm](https://hub.docker.com/u/seleniarm)，跟原本的 selenium 差在最後結尾 ```um``` 被替換為 ```arm```，呼應這個專案是為了解決 ARM 架構需求。但目前只有 Chromium 與 Firefox 有 ARM64 的 binary，所以 Node 只有支援這兩個瀏覽器，詳細原因可參考作者在 SeleniumHQ/docker-selenium 的 issue [armhf docker image of Selenium](https://github.com/SeleniumHQ/docker-selenium/issues/1076#issuecomment-1001055386) 中的說明。

## How to run

### Standalone

瀏覽器可試需求調整，啟動後可進入 Hub [http://localhost:4444](http://localhost:4444) 檢視

#### AMD64

```bash
docker run -d -p 4444:4444 -p 5900:5900 --shm-size="2g" selenium/standalone-chrome:4.1.1-20211217
```

#### ARM64

```bash
docker run -d -p 4444:4444 -p 5900:5900 --shm-size="2g" seleniarm/standalone-chromium:4.0.0-20211213
```

### Hub + Node

瀏覽器可試需求調整，啟動後可進入 Hub [http://localhost:4444](http://localhost:4444) 檢視

#### AMD64

```bash
docker-compose -f docker-compose.amd64.yaml up -d
```

#### ARM64

```bash
docker-compose -f docker-compose.arm64.yaml up -d
```

### Test

驗證可以透過 Hub 正常派送任務給 Node，可以使用 VNC Viewer 連線進入 Node Container 中確認，以下使用 Python 測試

1. 安裝 [python selenium package](https://pypi.org/project/selenium/)
2. 執行 Python Script

    ```python
    from selenium import webdriver

    driver = webdriver.Remote(command_executor='http://localhost:4444')
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    ```

## Reference

1. [docker-selenium](https://github.com/SeleniumHQ/docker-selenium)
