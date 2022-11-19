from bson import ObjectId

# Pydantic
from pydantic import BaseModel


class JokeBase(BaseModel):
    joke: str


class JokeOut(JokeBase):
    owner: str
    joke: str


class JokeInner(JokeBase):
    _id: ObjectId()
