import time

import pytest

from reqres import NewUser


@pytest.fixture()
def test_data(username, userjob):
    return {"name": username, "job": userjob}


def test_response_content(client, test_data):
    """Tests that POST request returns `id` and `createdAt` values"""
    response = client.post("/api/users", json=test_data)

    assert response.status_code == 201
    assert response.json().get("id")
    assert response.json().get("createdAt")


@pytest.mark.parametrize("request_time", [95, 100, 105, 110])
def test_response_time(client, test_data, request_time):
    """Tests that response time for POST request is less than 100"""
    start = time.perf_counter()
    response = client.post("/api/users", json=test_data)
    elapsed_time_ms = (time.perf_counter() - start) * 1000

    assert response.status_code == 201
    assert elapsed_time_ms < request_time


def test_response_schema(client, test_data):
    """Verifies correct schema for response by mapping response to a NewUser dataclass"""
    response = client.post("/api/users", json=test_data)
    assert NewUser(**response.json()), "Response cannot be matched to schema for a new user"
