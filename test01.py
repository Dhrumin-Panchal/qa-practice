# pytest version — cleaner, professional
import requests

def test_user_has_name():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert r.status_code == 200
    assert "name" in r.json()

def test_user_has_email():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert "email" in r.json()