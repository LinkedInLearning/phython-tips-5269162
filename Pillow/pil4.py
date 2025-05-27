from PIL import Image
import os
basisverzeichnis = os.path.dirname(os.path.abspath(__file__))

# Beispiel: Öffne eine Datei im Unterordner 'images' neben dem aktuellen Skript
dateipfad = os.path.join(basisverzeichnis, 'images', 'b1.jpeg')
bild = Image.open(dateipfad)
gedreht = bild.rotate(90)  # im Uhrzeigersinn
horizontal = bild.transpose(Image.FLIP_LEFT_RIGHT)
vertikal = bild.transpose(Image.FLIP_TOP_BOTTOM)

gedreht.show()
horizontal.show()
vertikal.show()