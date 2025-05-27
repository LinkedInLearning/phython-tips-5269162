import psutil

# Partitionen anzeigen
for part in psutil.disk_partitions():
    print(f"Gerät: {part.device}, Einhängepunkt: {part.mountpoint}, Typ: {part.fstype}")

# Festplattennutzung
disk = psutil.disk_usage('/')
print(f"Gesamt: {disk.total / (1024**3):.2f} GB")
print(f"Benutzt: {disk.used / (1024**3):.2f} GB")
print(f"Frei: {disk.free / (1024**3):.2f} GB")
print(f"Auslastung: {disk.percent}%")

# Festplatten-I/O
disk_io = psutil.disk_io_counters()
print(f"Lesen: {disk_io.read_bytes / (1024**2):.2f} MB, Schreiben: {disk_io.write_bytes / (1024**2):.2f} MB")
