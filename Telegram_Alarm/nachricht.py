import RPi.GPIO as GPIO
import time
import requests

# Telegram Bot config
TOKEN = ''
CHAT_ID = ''

# GPIO Setup
PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.get(url, params=payload)

try:
    print("Warte auf Bewegung...")
    while True:
        if GPIO.input(PIR_PIN):
            print("Bewegung erkannt!")
            send_telegram_message("Bewegung erkannt am Raspberry Pi!")
            time.sleep(5)  # kurze Pause, um Spam zu vermeiden
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Beende...")
finally:
    GPIO.cleanup()
