from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b"TEST CD CD CD Hello, World ! TEST TEST TEST TEST"
