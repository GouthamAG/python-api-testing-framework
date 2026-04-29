from utils.api_client import APIClient

# client = APIClient()

def test_get_users(client):
    response = client.get("/users?page=2")

    assert response.status_code == 200
    assert "data" in response.json()


def test_non_existing_user(client):
    response = client.get("users/xya")

    assert response.status_code == 404

    content_type = response.headers.get("Content-Type", "").lower()
    print(content_type) #text/html; charset=utf-8

    if "application/json" in content_type:
        assert response.json() == {}
    else:
        assert "<html" in response.text.lower()


def test_create_user(client):
    payload = {
        "name" : "Goutham",
        "job" : "Tester"
    }

    response = client.post("/users", payload=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Goutham"