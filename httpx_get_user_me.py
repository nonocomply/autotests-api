import httpx


login_payload = {
    "email": "user1@example.com",
    "password": "string",
}

login_response = httpx.post(
    url="http://localhost:8000/api/v1/authentication/login", json=login_payload
)
assert login_response.status_code == 200
login_response_data = login_response.json()


token = login_response_data["token"].get("accessToken")
header = {"Authorization": f"Bearer {token}"}

me_response = httpx.get(url="http://localhost:8000/api/v1/users/me", headers=header)
assert me_response.status_code == 200
me_response_data = me_response.json()
print(me_response_data)
