import redis
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/count")
def count():
    # redis container 與 api container 在同一個 Compose 中，所以可以直接用 Compose 的名稱當 host 溝通
    # 也因為在同一個 Compose 中，Container 間 port 是完全互通的，不用做 port 設定，也不需要 Expose
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    if r.exists('count'):
        r.set('count', int(r.get('count'))+1)
    else:
        r.set('count', 0)
    return {"count": r.get('count')}
