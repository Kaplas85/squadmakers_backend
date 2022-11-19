# Python
import random

# FastAPI
from fastapi.testclient import TestClient

# App
from main import app

client = TestClient(app)


def test_sum():
    TEST_NUMBER = random.randint(10, 100)
    response = client.get("/math/sum/", params={"number": TEST_NUMBER})
    RESULT = response.json()["result"]

    assert response.status_code == 200
    assert TEST_NUMBER + 1 == int(RESULT)


def test_lcm():
    NUMBER_LISTS = [100, 3, 24, 32, 1]
    response = client.get("/math/lcm/", params={"numbers": NUMBER_LISTS})
    RESULT = response.json()["lcm"]
    assert response.status_code == 200
    assert RESULT == 2400
