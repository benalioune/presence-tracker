from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_session_success():
    res = client.post("/sessions",headers={
        "Authorization": f"Bearer"
    })