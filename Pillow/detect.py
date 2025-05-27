import cv2
import os
basisverzeichnis = os.path.dirname(os.path.abspath(__file__))

# Beispiel: Öffne eine Datei im Unterordner 'images' neben dem aktuellen Skript
dateipfad = os.path.join(basisverzeichnis, 'images', 'b3.jpg')

bild = cv2.imread(dateipfad)
grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)

gesichter_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gesichter = gesichter_cascade.detectMultiScale(grau, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in gesichter:
    cv2.rectangle(bild, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Gesichter", bild)
cv2.waitKey(0)
cv2.destroyAllWindows()
