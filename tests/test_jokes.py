# FastAPI
from fastapi.testclient import TestClient

# App
from main import app

client = TestClient(app)


BAD_ID = "63784423d0aaf6b3f8bbFFFF"
INVALID_ID = "223344"
created_joke_id = ""


def test_chuck():
    response = client.get("/jokes/", params={"owner": "chuck"})
    assert response.status_code == 200


def test_dad():
    response = client.get("/jokes/", params={"owner": "dad"})
    assert response.status_code == 200


def test_without_params():
    response = client.get("/jokes/")
    assert response.status_code == 200


def test_joke_with_bad_owner():
    response = client.get("/jokes/", params={"owner": "dada"})
    assert response.status_code == 400


def test_list_all_created_jokes_empty():
    response = client.get("/jokes/created")

    assert response.status_code == 404


def test_create_joke():
    response = client.post("/jokes/", json={"joke": "A random joke"})

    assert response.status_code == 201


def test_list_all_created_jokes_with_items():
    response = client.get("/jokes/created")
    assert response.status_code == 200


def test_update_joke_with_good_id():
    ID = client.get("/jokes/created").json()[0]["_id"]
    response = client.put(f"/jokes/{ID}", json={"joke": "a updated joke"})
    assert response.status_code == 200


def test_update_joke_with_bad_id():
    response = client.put(f"/jokes/{BAD_ID}", json={"joke": "a updated joke"})
    assert response.status_code == 404


def test_update_joke_with_invalid_id():
    response = client.put(f"/jokes/{INVALID_ID}", json={"joke": "a updated joke"})
    assert response.status_code == 400


def test_delete_joke_with_good_id():
    ID = client.get("/jokes/created").json()[0]["_id"]
    response = client.delete(f"/jokes/{ID}")
    assert response.status_code == 200


def test_update_joke_with_bad_id():
    response = client.delete(f"/jokes/{BAD_ID}")
    assert response.status_code == 404


def test_update_joke_with_invalid_id():
    response = client.delete(f"/jokes/{INVALID_ID}")
    assert response.status_code == 400
