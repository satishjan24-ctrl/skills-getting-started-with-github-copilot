import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_for_activity():
    # Use a known activity and email
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    signup_url = f"/activities/{activity_name}/signup?email={email}"
    response = client.post(signup_url)
    assert response.status_code == 200 or response.status_code == 400
    # Try signing up again to check duplicate prevention
    response2 = client.post(signup_url)
    assert response2.status_code == 400
    assert "already registered" in response2.json().get("detail", "")
