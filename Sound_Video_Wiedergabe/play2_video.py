from pathlib import Path
import time
import os

# VLC-Installationspfad setzen (achte auf 32- vs. 64-bit!)
vlc_path = r"C:\Program Files\VideoLAN\VLC"
os.environ['PATH'] = vlc_path + os.pathsep + os.environ['PATH']

import vlc  # Jetzt nach dem PATH-Update

# VLC initialisieren
instance = vlc.Instance('--no-xlib')
player = instance.media_player_new()

# Pfad zum Video
basisverzeichnis = Path(__file__).resolve().parent
videopfad = basisverzeichnis / "videos" / "video1.mp4"
media = instance.media_new(str(videopfad))  # wichtig: in string umwandeln!
player.set_media(media)

# Video starten
player.play()

# kurz warten, damit das Video abgespielt wird
time.sleep(30)
