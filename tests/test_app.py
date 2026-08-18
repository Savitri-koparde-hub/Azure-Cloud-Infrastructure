import os
import tempfile
import app as vision_app

def test_home():
    db = tempfile.NamedTemporaryFile(delete=False)
    db.close()
    old_path = vision_app.DB_PATH
    vision_app.DB_PATH = db.name
    vision_app.init_db()

    client = vision_app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200

    vision_app.DB_PATH = old_path
    os.unlink(db.name)

def test_health():
    client = vision_app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
