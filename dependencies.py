# Requests
import requests

# CONST
CHUCK_API: str = "https://api.chucknorris.io/jokes/random"
DAD_API: str = "https://icanhazdadjoke.com/"


async def get_external_jokes(owner: str) -> str:

    HEADERS = {"accept": "application/json"}

    if owner == "chuck":
        BASE_URL = CHUCK_API
    elif owner == "dad":
        BASE_URL = DAD_API
    else:
        raise ValueError(f"The owner {owner} not exists.")

    req = requests.get(BASE_URL, headers=HEADERS).json()

    if owner == "chuck":
        response = req["value"]
    elif owner == "dad":
        response = req["joke"]

    return response
