from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import date
import logging
from basemodel import User

app = FastAPI()

_sample_users = [
    {"id": 1, "name": "james1", "birthdate": "2000-01-01"},
    {"id": 2, "name": "james2", "birthdate": "2001-02-02"},
    {"id": 3, "name": "james3", "birthdate": "2002-03-03"}
]

# Logger 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API 엔드포인트 정의
@app.post("/api/users")
def create_user(user: User):
    # TODO: 유저 생성 구현
    return {"message": "User successfully created."}

@app.get("/api/users/{user_id}")
def read_user(user_id: int):
    user = None
    for _user_data in _sample_users:
        if _user_data['id'] == user_id:
            user = User(**_user_data)
    return user

# 아티스트와 노래 API 추가 (이하 유사한 방식으로 추가 가능)
@app.get("/api/artists")
def list_all_artists():
    return {"message": "A list of all artists."}

@app.get("/api/artists/{artist_id}")
def get_artist_details(artist_id: int):
    return {"message": f"Details of the artist with id {artist_id}."}

@app.get("/api/songs")
def list_all_songs():
    return {"message": "A list of all songs."}

# 로거를 통한 로깅
@app.middleware("http")
async def add_logger(request: Request, call_next):
    logger.info(f"Request to {request.method} {request.url}")
    response = await call_next(request)
    return response