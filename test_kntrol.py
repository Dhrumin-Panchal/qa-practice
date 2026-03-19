import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# ─── Fixtures ───────────────────────────────────────────

@pytest.fixture
def user():
    return requests.get(f"{BASE_URL}/users/1").json()

@pytest.fixture
def post():
    return requests.get(f"{BASE_URL}/posts/1").json()

# ─── Auth ───────────────────────────────────────────────

def test_auth_user_exists(user):
    assert user is not None

def test_auth_user_has_username(user):
    assert "username" in user

# ─── Partner Management ─────────────────────────────────

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_partner_profile_status(user_id):
    r = requests.get(f"{BASE_URL}/users/{user_id}")
    assert r.status_code == 200

def test_partner_has_name(user):
    assert "name" in user

def test_partner_has_email(user):
    assert "email" in user

def test_partner_has_phone(user):
    assert "phone" in user

# ─── Records ────────────────────────────────────────────

def test_get_record_status(post):
    assert post is not None

def test_get_record_has_title(post):
    assert "title" in post

def test_get_record_has_body(post):
    assert "body" in post

def test_create_record():
    payload = {"title": "QA Test", "body": "Automated", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201
    assert "id" in r.json()

def test_update_record():
    r = requests.patch(f"{BASE_URL}/posts/1", json={"title": "Updated"})
    assert r.status_code == 200

def test_delete_record():
    r = requests.delete(f"{BASE_URL}/posts/1")
    assert r.status_code == 200