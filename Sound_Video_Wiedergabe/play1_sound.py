from pathlib import Path
import pygame

# Pfad zur MP3
basisverzeichnis = Path(__file__).resolve().parent
mp3pfad = basisverzeichnis / "sounds" / "saturday.ogg"

# MP3 abspielen
if mp3pfad.exists():
    pygame.mixer.init()
    pygame.mixer.music.load(str(mp3pfad))
    pygame.mixer.music.play()
    input("Drücke Enter, um das Programm zu beenden...")
else:
    print(f"Sounddatei nicht gefunden: {mp3pfad}")
