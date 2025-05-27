
import os
import subprocess

input_folder="musik_in/"

output_folder="musik_out/"

def loudnorm_ffmpeg(input_path, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-ar", "44100",
        "-ac", "2",
        "-b:a", "192k",
        output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

# Durchlaufe OGG- und MP3-Dateien
try:
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3") or filename.endswith(".ogg") :
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            print(f"Normalisiere (LUFS): {filename}")
            loudnorm_ffmpeg(input_path, output_path)

    print("LUFS-Normalisierung abgeschlossen.")

except:
    print("Fehler bei der Normalisierung")
