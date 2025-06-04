import httpx

url = "http://localhost:8000/"
api_path = "api/v1/authentication/"
request_url = url + api_path

login_payload = {
    "email": "user1@example.com",
    "password": "string",
}

login_response = httpx.post(url=request_url + "login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

refresh_payload = {"refreshToken": login_response_data["token"]["refreshToken"]}

refresh_response = httpx.post(url=request_url + "refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)
