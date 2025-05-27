import requests
from bs4 import BeautifulSoup

response = requests.get("https://blog.rjs.de")
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("title")
print(title.get_text())  # Gibt den Titel der Webseite aus
