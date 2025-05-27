import requests

response = requests.get("https://rjs.de/index.php")

# Liste aller möglichen bekannten Attribute/Members 
attributes = [
    "status_code", "headers", "text", "content", "json", "ok", "url", "cookies",
    "encoding", "elapsed", "history", "is_permanent_redirect", "is_redirect",
    "links", "next", "reason", "request", "raw"
]

print("Eigenschaften des response-Objekts:")
for attr in attributes:
    if hasattr(response, attr):
        try:
            value = getattr(response, attr)
            # Methodenaufrufe nur, wenn nötig (z. B. json())
            if callable(value):
                value = value()
            print(f"{attr}: {value}")
        except Exception as e:
            print(f"{attr}: <Fehler beim Zugriff – {e}>")
    else:
        print(f"{attr}: <nicht vorhanden>")
