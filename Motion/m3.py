import RPi.GPIO as GPIO
import time
from datetime import datetime
from pathlib import Path

skript_verzeichnis = Path(__file__).resolve().parent

log_file_path=skript_verzeichnis / "log" /"bewegung_log.txt"
# Setup für den Raspberry Pi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # GPIO 17 als Eingang mit Pull-Down-Widerstand

# Initialisieren von Variablen
bewegung_zaehler = 0


print("Sensor bereit...")

def log_bewegung(timestamp):
    """Schreibt die Bewegung in eine Log-Datei mit Timestamp"""
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{timestamp} - Bewegung erkannt!\n")
    print(f"Bewegung um {timestamp} protokolliert.")

try:
    while True:
        # Prüfe den Zustand des Sensors
        sensor_status = GPIO.input(17)

        if sensor_status == GPIO.HIGH:
            # Bewegung erkannt
            bewegung_zaehler += 1
            print(f"Bewegung erkannt! ({bewegung_zaehler} hintereinander)")

            # Wenn mehr als 3 Bewegungen hintereinander erkannt wurden
            if bewegung_zaehler > 3:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_bewegung(timestamp)  # Logge die Bewegung in eine Datei
                bewegung_zaehler = 0  # Zähler zurücksetzen
        else:
            # Keine Bewegung
            print("Keine Bewegung erkannt.")
            bewegung_zaehler = 0  # Zähler zurücksetzen, wenn keine Bewegung erkannt wurde
        
        time.sleep(0.5)  # Sensor nur zweimal pro Sekunde abfragen

except KeyboardInterrupt:
    # Aufräumen bei Programmabbruch
    GPIO.cleanup()
    print("Programm beendet.")
