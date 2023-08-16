from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    birthdate: str  # 간단함을 위해 문자열 사용

_sample_users = [
    {"id": 1, "name": "james1", "birthdate": "2000-01-01"},
    {"id": 2, "name": "james2", "birthdate": "2001-02-02"},
    {"id": 3, "name": "james3", "birthdate": "2002-03-03"}
]

@app.post("/api/users")
def create_user(user: User):
    # 새로운 사용자를 생성하기 위한 구현
    return {"message": "사용자가 성공적으로 생성되었습니다."}

@app.get("/api/users/{user_id}")
def read_user(user_id: int):
    user = None
    for _user_data in _sample_users:
        if _user_data['id'] == user_id:
            user = User(**_user_data)
    return user

@app.put("/api/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    # 사용자 데이터를 user_id로 업데이트하기 위한 구현
    return {"message": "사용자가 성공적으로 업데이트되었습니다."}

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    # 사용자를 user_id로 삭제하기 위한 구현
    return {"message": "사용자가 성공적으로 삭제되었습니다."}

@app.get("/api/albums/{album_id}")
def read_album(album_id: int):
    # album_id로 앨범을 가져오기 위한 구현
    return album_data

@app.get("/api/albums")
def get_all_albums():
    # 모든 앨범을 가져오기 위한 구현
    return all_albums_data

# artists, genres, and reviews에 대한 유사한 엔드포인트

@app.get("/api/artists")
def list_all_artists():
    # API로 모든 아티스트를 나열합니다.
    return {"message": "모든 아티스트 목록입니다."}

@app.get("/api/artists/{artist_id}")
def get_artist_details(artist_id: int):
    # 특정 아티스트의 세부 정보를 쿼리하는 API
    return {"message": f"id가 {artist_id}인 아티스트의 세부 정보입니다."}

@app.get("/api/songs")
def list_all_songs():
    # API로 모든 노래를 나열합니다.
    return {"message": "모든 노래 목록입니다."}