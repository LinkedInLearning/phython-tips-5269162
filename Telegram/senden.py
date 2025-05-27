import requests

# Telegram Bot config
TOKEN = ''
CHAT_ID = ''

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == '__main__':
    result = send_message("Neue Test-Nachricht!")
    print(result)
