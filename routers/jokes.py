# Python
import random

# FastAPI
from fastapi import APIRouter, Query, HTTPException, Body, Path

# Squemas
from squemas import jokes

# Database
from db.connect import db
from bson import ObjectId
from bson.errors import InvalidId

# Dependencies
from dependencies import get_external_jokes

# Helpers
from helper import process_response, check_if_item_exists


router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.get(
    "/",
    responses={400: {"description": "The owner value not exists"}},
    response_model=jokes.JokeOut,
)
async def get_jokes(owner: str | None = Query(None, max_length=5)):

    OWNERS_LIST = ["chuck", "dad"]

    if isinstance(owner, str) and owner in OWNERS_LIST:
        joke: str = await get_external_jokes(owner)
        response = {"owner": owner, "joke": joke}
    elif isinstance(owner, str) and owner not in OWNERS_LIST:
        raise HTTPException(
            status_code=400,
            detail=f"The owner value '{owner}' not exists",
        )
    else:
        SELECTED_OWNER = random.choice(OWNERS_LIST)
        joke: str = await get_external_jokes(SELECTED_OWNER)
        response = {"owner": SELECTED_OWNER, "joke": joke}

    return response


@router.get("/created", name="List All Jokes Created")
async def list_all_jokes():

    documents = list(db.jokes.find({}))
    return process_response(documents)


@router.post(
    "/",
    responses={
        400: {"description": "Has ocurred a error creating the joke. Try Again"},
        201: {"description": "Joke was created!"},
    },
    status_code=201,
)
async def create_jokes(joke: jokes.JokeBase = Body(...)):
    try:
        db.jokes.insert_one(dict(joke))
    except:
        raise HTTPException(400, "Has ocurred a error creating the joke. Try Again")
    return {"message": "joke created"}


@router.put(
    "/{joke_id}/",
    responses={400: {"description": "Joke not exists or the ID is invalid"}},
)
async def update_joke(
    joke_id: str = Path(..., title="Joke ID"),
    data: jokes.JokeBase = Body(..., title="Joke content"),
):
    new_data = dict(data)

    try:
        if not check_if_item_exists(db, "jokes", joke_id):
            raise HTTPException(400, "Joke not exists.")

        db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"joke": new_data["joke"]}},
        )

        return {"message": "Joke updated"}
    except InvalidId:
        raise HTTPException(400, "The ID pased is invalid")


@router.delete(
    "/{joke_id}/",
    responses={400: {"description": "Joke not exists or the ID is invalid"}},
)
async def delete_joke(joke_id: str = Path(..., title="Joke ID")):

    try:
        if not check_if_item_exists(db, "jokes", joke_id):
            raise HTTPException(400, "Joke not exists.")

        db.jokes.delete_one({"_id": ObjectId(joke_id)})
        return
    except InvalidId:
        raise HTTPException(400, "The ID pased is invalid")
