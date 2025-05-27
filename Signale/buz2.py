import RPi.GPIO as GPIO
import time

# Pin-Definition (ändern Sie dies nach Ihrer Verdrahtung)
buzzer_pin = 17

# Definition von Noten und ihren Frequenzen (in Hz)
noten = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25
}

# Definition einer einfachen Melodie (Liste von Tupeln: (Note, Dauer in Sekunden))
melodie = [
    ('C4', 0.5),
    ('D4', 0.5),
    ('E4', 0.5),
    ('C4', 0.5),
    ('E4', 0.5),
    ('F4', 0.5),
    ('G4', 1.0),
    ('G4', 0.5),
    ('F4', 0.5),
    ('E4', 0.5),
    ('D4', 0.5),
    ('C4', 1.0)
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

    print("Spiele Melodie...")
    for note, dauer in melodie:
        print(f"Spiele Note: {note} ({noten[note]:.2f} Hz) für {dauer} Sekunde(n)")
        beep(buzzer_pin, noten[note], dauer)
        time.sleep(0.1)  # Kurze Pause zwischen den Noten

    print("Melodie beendet.")

finally:
    GPIO.cleanup()
