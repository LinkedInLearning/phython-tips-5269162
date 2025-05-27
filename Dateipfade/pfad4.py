from pathlib import Path

skript_verzeichnis = Path(__file__).resolve().parent
dateipfad = skript_verzeichnis / "daten" / "input" / "beispiel.txt"

print(dateipfad)

if dateipfad.exists():
    print("Datei gefunden.")
