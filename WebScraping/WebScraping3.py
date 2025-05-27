import requests
from bs4 import BeautifulSoup

url = "https://blog.rjs.de"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Alle Artikel (häufig in <article> Tags bei WordPress-Blogs)
articles = soup.find_all("article")

for article in articles:
    # Titel (häufig in einem <h2> oder <h1> mit <a>)
    title_tag = article.find(["h1", "h2", "h3"])
    if title_tag and title_tag.a:
        title = title_tag.get_text(strip=True)
        link = title_tag.a["href"]
    else:
        title = "Kein Titel gefunden"
        link = "Kein Link gefunden"

    # Datum (häufig in einem <time> Tag)
    date_tag = article.find("time")
    if date_tag:
        date = date_tag.get("datetime", date_tag.get_text(strip=True))
    else:
        date = "Kein Datum gefunden"

    print(f"Titel: {title}")
    print(f"Datum: {date}")
    print(f"Link: {link}")
    print("-" * 40)
