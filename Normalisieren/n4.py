
import os
from pydub import AudioSegment
from pydub.effects import normalize
from pathlib import Path

skript_verzeichnis = Path(__file__).resolve().parent

in_dat=skript_verzeichnis / "musik_in" 
out_dat=skript_verzeichnis /"musik_out" 

# Durchlaufe MP3-Dateien
try:
    for filename in os.listdir(in_dat):
        if filename.endswith(".mp3") or filename.endswith(".ogg"):
            input_path = os.path.join(in_dat, filename)
            output_path = os.path.join(out_dat, filename)

            print(f"Verarbeite: {filename}")
            if filename.endswith(".ogg"):
                audio = AudioSegment.from_file(input_path, format="ogg")
            elif filename.endswith(".mp3"):
                audio = AudioSegment.from_file(input_path, format="mp3")
            normalized_audio = normalize(audio)
            normalized_audio.export(output_path, format="mp3")

except:
    print("Fehler bei der Normalisierung")
