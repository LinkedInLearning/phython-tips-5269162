import requests

url = "https://httpbin.org/get"

params = {
    "username": "max",
    "password": "geheim"
}

response = requests.get(url, params=params)

print("Status-Code:", response.status_code)
print("Antwort:", response.json())
