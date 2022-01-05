FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y netcat && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]
