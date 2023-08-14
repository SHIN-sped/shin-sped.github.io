from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class User(BaseModel):
    id: int
    name: str
    #email: str
    #password: str
    birthdate: date
    #gender: str
    #address: str
    #phone_num: str
    #social_media: str
    
class Music(BaseModel):
    id: int
    name: str
    birthdate: date