import RPi.GPIO as GPIO
import time

# Pin-Definition (ändern Sie dies nach Ihrer Verdrahtung)
buzzer_pin = 17

# Frequenz des gewünschten Tons (Hz)
frequency = 440  # A4 Note

# Dauer des Tons (Sekunden)
duration = 1

def beep(pin, freq, dur):
    period = 1.0 / freq
    delay = period / 2
    cycles = int(dur * freq)
    for i in range(cycles):
        GPIO.output(pin, True)
        time.sleep(delay)
        GPIO.output(pin, False)
        time.sleep(delay)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    beep(buzzer_pin, frequency, duration)

finally:
    GPIO.cleanup()
