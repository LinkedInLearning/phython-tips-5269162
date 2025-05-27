import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up aktivieren

print("Sensor bereit...")

try:
    while True:
        if GPIO.input(17):
            print("💡 Bewegung erkannt!")
        else:
            print("...")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
