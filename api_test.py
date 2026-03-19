import requests

passed = 0
failed = 0

def check(name, condition):
    global passed, failed
    if condition:
        print(f"  PASS  {name}")
        passed += 1
    else:
        print(f"  FAIL  {name}")
        failed += 1

# --- Test 1: Health Check ---
print("Health Check")
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
check("Status is 200", r.status_code == 200)
check("Response has id", "id" in r.json())
print()

# --- Test 2: Get Partner Profile ---
print("Partner Profile")
r2 = requests.get("https://jsonplaceholder.typicode.com/users/1")
check("Status is 200", r2.status_code == 200)
check("Has name field", "name" in r2.json())
check("Has email field", "email" in r2.json())
print()

# --- Test 3: Create Record ---
print("Create Record")
payload = {"title": "Test Entry", "body": "QA automation test", "userId": 1}
r3 = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
check("Status is 201", r3.status_code == 201)
check("Response has id", "id" in r3.json())
print()

# --- Summary ---
print(f"Results: {passed} passed, {failed} failed")