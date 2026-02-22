from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


def test_root_endpoint_has_project_banner():
    r = client.get("/")
    assert r.status_code == 200
    body = r.json()
    assert body.get("project") == "api-security-lab"
