from PIL import Image
import os
basisverzeichnis = os.path.dirname(os.path.abspath(__file__))

# Beispiel: Öffne eine Datei im Unterordner 'images' neben dem aktuellen Skript
dateipfad = os.path.join(basisverzeichnis, 'images', 'b1.jpeg')
bild = Image.open(dateipfad)
graustufen = bild.convert("L")  # "L" = Luminanz, also Graustufen

graustufen.show()