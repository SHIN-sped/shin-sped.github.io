# Define Pydantic models
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int
    name: str
    birthdate: date

class Music(BaseModel):
    id: int
    name: str
    birthdate: date

class Album(BaseModel):
    id: int
    name: str
    release_date: date

class Artist(BaseModel):
    id: int
    name: str
    nationality: str