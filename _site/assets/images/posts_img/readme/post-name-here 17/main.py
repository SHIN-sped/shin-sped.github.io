from fastapi import FastAPI
from pydantic import BaseModel
#from dto.my_dto import User, Music
from datetime import date, datetime, time, timedelta
# pydantic DTO data transfer object server-client
# react with JWT token
_sample_users = [
                {"id": 1, "name": "james1", "birthdate": date.today()},
                {"id": 2, "name": "james2", "birthdate": date.today()},
                {"id": 3, "name": "james3", "birthdate": date.today()}
]    

class User(BaseModel):
    id: int
    name: str
    #email: str
    #password: str
    birthdate: date
    #gender: str
    address: str = None
    #phone_num: str
    #social_media: str
app = FastAPI()
@app.get("/") # GET 요청 root로 들어오면 메세지
async def root():
    return {"message": "Hello World"}

# @app.get("/items/{item_id}") # 경로 매개변순
# async def read_item(item_id):
#     return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int): # 타입이 있는 매개변수
    return {"item_id": item_id}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = None
    for _user_data in _sample_users:
        if _user_data['id'] == user_id:
            user = User(**_user_data) # 키와 매핑 되는 모든 것들을 연산
    return user