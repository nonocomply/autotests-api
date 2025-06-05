import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

create_user_response = httpx.post(
    url="http://127.0.0.1:8000/api/v1/users", json=create_user_payload
)
assert create_user_response.status_code == 200, "User wasn't created"
create_user_response_data = create_user_response.json()


login_payload = {
    "email": create_user_payload.get("email"),
    "password": create_user_payload.get("password"),
}
login_response = httpx.post(
    url="http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload
)
assert login_response.status_code == 200
login_response_data = login_response.json()

token = login_response_data["token"].get("accessToken")
header = {"Authorization": f"Bearer {token}"}

me_response = httpx.get(url="http://localhost:8000/api/v1/users/me", headers=header)
assert me_response.status_code == 200
me_response_data = me_response.json()

user_id = me_response_data["user"].get("id")

update_user_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
update_user_response = httpx.patch(
    url=f"http://localhost:8000/api/v1/users/{user_id}",
    json=update_user_payload,
    headers=header,
)
assert update_user_response.status_code == 200
update_user_response_data = update_user_response.json()

print(update_user_response_data)
