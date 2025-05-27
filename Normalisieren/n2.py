from pydub import AudioSegment
from pydub.effects import normalize
from pathlib import Path

skript_verzeichnis = Path(__file__).resolve().parent

in_dat=skript_verzeichnis / "musik_in" 
out_dat=skript_verzeichnis /"musik_out" 
dat = input("Eingabe der Musikdatei:\n")
in_dat=str(in_dat) + "/" + dat

out_dat=str(out_dat) + "/normalized_"+dat
print(in_dat, out_dat)
def audio_info(audio):
    print("-" * 50)
    print("Dauer (s):", audio.duration_seconds)
    print("Samplerate:", audio.frame_rate)
    print("Kanäle:", audio.channels)
    print("Sample-Width (Bytes):", audio.sample_width)
    print("Durchschnittliche Lautheit (dBFS):", audio.dBFS)
    print("Frames:", audio.frame_count())
    print("-" * 50)
try:
    if in_dat.endswith(".ogg"):
        audio = AudioSegment.from_file(in_dat, format="ogg")
    elif in_dat.endswith(".mp3"):
        audio = AudioSegment.from_file(in_dat, format="mp3")
        
    print(f"Datei {in_dat} geladen")
    audio_info(audio)

    # Normalisieren
    normalized_audio = normalize(audio)
    print(f"Datei {in_dat} normalisiert")
    # Als MP3 speichern
    normalized_audio.export(out_dat, format="mp3")
    # Als OGG speichern
    normalized_audio.export(out_dat, format="ogg")
    print(f"Datei unter {out_dat} exportiert")
    audio_info(normalized_audio)
except:
    print("Fehler bei der Normalisierung")
