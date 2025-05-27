import os
def find_venvs(start_path):
    for root, dirs, files in os.walk(start_path):
        if "pyvenv.cfg" in files:
            print("Venv gefunden in:", root)

# Beispielpfade:
paths = [
    os.path.expanduser("~"),           # Home-Verzeichnis
    os.path.expanduser("~/venvs"),     # typischer venv-Ordner (Linux/macOS)
    "C:\\venvs",                        # Windows
    "D:\\"

]

for path in paths:
    if os.path.exists(path):
        find_venvs(path)
