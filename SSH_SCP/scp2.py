import subprocess

# Datei hochladen
subprocess.run([
    "scp",
    "kultur.txt",
    "trillian@192.168.13.246:/home/trillian/kultur.txt"
])

# Datei herunterladen
subprocess.run([
    "scp",
    "trillian@192.168.13.246:/home/trillian/kultur.txt",
    "erlk3.txt"
])

