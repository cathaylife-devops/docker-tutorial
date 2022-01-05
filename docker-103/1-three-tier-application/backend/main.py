from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import User as ModelUser
from schema import User as SchemaUser
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.post("/api/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user

@app.get("/api/users/", response_model=List[SchemaUser])
def get_users():
    users = db.session.query(ModelUser).all()
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
