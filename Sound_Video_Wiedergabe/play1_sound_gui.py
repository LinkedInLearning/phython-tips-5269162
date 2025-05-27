import pygame
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Fenster erstellen
fenster = tk.Tk()
fenster.title("Musikplayer")
fenster.geometry("300x150")

# Pygame-Mixer initialisieren
pygame.mixer.init()

def musik_auswählen():
    dateipfad = filedialog.askopenfilename(
        title="Musikdatei auswählen",
        filetypes=[("Audio-Dateien", "*.mp3 *.ogg *.wav")]
    )

    if not dateipfad:
        return  # Abbrechen

    try:
        pygame.mixer.music.load(dateipfad)
        pygame.mixer.music.play()
        status_label.config(text=f"Spiele: {Path(dateipfad).name}")
    except Exception as e:
        messagebox.showerror("Fehler", f"Die Datei konnte nicht abgespielt werden:\n{e}")

def musik_stoppen():
    pygame.mixer.music.stop()
    status_label.config(text="Musik gestoppt")

# GUI-Elemente
auswahl_button = tk.Button(fenster, text="Musik wählen", command=musik_auswählen)
auswahl_button.pack(pady=10)

stop_button = tk.Button(fenster, text="Stopp", command=musik_stoppen)
stop_button.pack(pady=5)

status_label = tk.Label(fenster, text="Keine Musik ausgewählt")
status_label.pack(pady=10)

# Hauptloop starten
fenster.mainloop()
