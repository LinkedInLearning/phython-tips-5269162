from pathlib import Path
import cv2

# Pfad zum Video
basisverzeichnis = Path(__file__).resolve().parent
videopfad = basisverzeichnis / "videos" / "video1.mp4"

video = cv2.VideoCapture(videopfad)


while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()