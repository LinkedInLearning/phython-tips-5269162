import psutil

mem = psutil.virtual_memory()
print(f"Gesamtspeicher: {mem.total / (1024**3):.2f} GB")
print(f"Benutzt: {mem.used / (1024**3):.2f} GB")
print(f"Frei: {mem.available / (1024**3):.2f} GB")
print(f"Auslastung: {mem.percent}%")
