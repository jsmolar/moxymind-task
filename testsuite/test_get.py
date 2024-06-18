def test_response(client):
    """Tests that response contains `total` and `last_name` values for first two users"""
    response = client.get("api/users?page=2")
    assert response.status_code == 200

    assert response.json().get("total")

    assert len(response.json()["data"]) >= 2, f"Less than 2 users were returned in {response.json()}"
    assert response.json()["data"][0].get("last_name")
    assert response.json()["data"][1].get("last_name")


def test_total(client):
    """Tests that total value per page equals to total users located in data"""
    response = client.get("api/users?page=2")
    assert response.status_code == 200

    assert response.json()["per_page"] == len(response.json()["data"])
