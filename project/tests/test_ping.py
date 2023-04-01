from app import main
import os

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "ping": "pong",
        "testing": True,
        "database": os.environ['DATABASE_TEST_URL'],
    }
