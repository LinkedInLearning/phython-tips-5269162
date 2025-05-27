import requests
from bs4 import BeautifulSoup

response = requests.get("https://blog.rjs.de")
soup = BeautifulSoup(response.text, "html.parser")
images = soup.find_all("img")
for img in images:
    print(img.get("src"), img.get("alt"))
