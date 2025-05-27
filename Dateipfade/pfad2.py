import os

# Portabel einen Pfad zusammensetzen
skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))
dateipfad = os.path.join(skript_verzeichnis,"daten", "audio", "saturday.ogg")
print(dateipfad)
