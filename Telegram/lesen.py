import requests
TOKEN = ''

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)
data = response.json()

# Alle Nachrichten anzeigen
for update in data['result']:
    print(update['message']['chat']['id'], ":", update['message']['text'])
