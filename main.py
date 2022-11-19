# FastAPI
from fastapi import FastAPI

# Routers
from routers import jokes, math

app = FastAPI()


app.include_router(jokes.router)
app.include_router(math.router)
