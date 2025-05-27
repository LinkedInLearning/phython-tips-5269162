from PIL import Image
import os

basisverzeichnis = os.path.dirname(os.path.abspath(__file__))

# Beispiel: Öffne eine Datei im Unterordner 'images' neben dem aktuellen Skript
dateipfad = os.path.join(basisverzeichnis, 'images', 'b1.jpeg')
bild = Image.open(dateipfad)
from PIL import ImageFilter

unscharf = bild.filter(ImageFilter.BLUR)
kante = bild.filter(ImageFilter.FIND_EDGES)

unscharf.show()
kante.show()
kante.save(os.getcwd() + "/images/neu.jpg") # Speichern
