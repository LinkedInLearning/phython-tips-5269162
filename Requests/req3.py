
import requests

url = "http://localhost/PythonPraxis/login.php"  # Test-Endpoint, der alles zurückgibt

data = {
    "username": "max",
    "password": "geheim"
}

response = requests.post(url, data=data)

print("Status-Code:", response.status_code)
print("Antwort:", response.json())
