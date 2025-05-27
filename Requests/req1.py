import requests

response = requests.get("https://rjs.de/index.php")
print(response.status_code)   # HTTP-Statuscode, z. B. 200
print(response.text)          # Antworttext (roh)
