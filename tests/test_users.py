from utils.api_client import APIClient

# client = APIClient()

def test_get_users(client):
    response = client.get("/users?page=2")

    assert response.status_code == 200
    assert "data" in response.json()


def test_create_user(client):
    payload = {
        "name" : "Goutham",
        "job" : "Tester"
    }

    response = client.post("/users", payload=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Goutham"