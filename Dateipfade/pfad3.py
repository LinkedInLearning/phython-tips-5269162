import os

# Portabel einen Pfad zusammensetzen
skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))
dateipfad = os.path.join(skript_verzeichnis,"daten", "audio", "monday.ogg")
if not os.path.exists(dateipfad):
    print("Datei nicht gefunden!")

# Verzeichnisse erstellen (wenn noch nicht vorhanden)
os.makedirs(os.path.join(skript_verzeichnis, "daten", "video"), exist_ok=True)


