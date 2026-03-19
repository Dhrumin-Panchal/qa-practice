import requests

passed = 0
failed = 0

def check(name, condition):
    global passed, failed
    if condition:
        print(f"    PASS  {name}")
        passed += 1
    else:
        print(f"    FAIL  {name}")
        failed += 1

# --- Loop through multiple users ---
user_ids = [1, 2, 3, 4, 5]

for uid in user_ids:
    print(f"Testing user ID: {uid}")
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{uid}")
    check(f"Status is 200", r.status_code == 200)
    check(f"Has name", "name" in r.json())
    check(f"Has email", "email" in r.json())
    print()

print(f"Results: {passed} passed, {failed} failed")