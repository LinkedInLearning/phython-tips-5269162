import RPi.GPIO as GPIO
import time

# Pin-Definitionen (ändern Sie diese nach Ihrer tatsächlichen Verdrahtung)
buzzer_pin = 17
pir_pin = 27

# Definition von Noten und ihren Frequenzen (in Hz)
noten = {
    'C5': 523.25,
    'G4': 392.00
}

# Definition der vereinfachten Alarm-Melodie (zwei Töne)
alarm_melodie = [
    ('C5', 0.3),
    ('G4', 0.3)
]

def beep(pin, freq, dur):
    if freq == 0:  # Stille
        time.sleep(dur)
        return
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
    GPIO.setup(pir_pin, GPIO.IN)

    print("Warte auf Bewegung...")

    while True:
        if GPIO.input(pir_pin):
            print("Bewegung erkannt!")
            print("Spiele Alarm...")
            for note, dauer in alarm_melodie:
                beep(buzzer_pin, noten.get(note, 0), dauer)
                time.sleep(0.1)  # Kurze Pause zwischen den Tönen
            time.sleep(2)  # Wartezeit nach dem Alarm
        time.sleep(0.1)  # Kurze Verzögerung in der Hauptschleife

finally:
    GPIO.cleanup()
