import psutil

# CPU-Auslastung (in Prozent) über alle Kerne
print("CPU-Auslastung:", psutil.cpu_percent(interval=1), "%")

# Auslastung pro CPU-Kern
print("CPU-Auslastung pro Kern:", psutil.cpu_percent(interval=1, percpu=True))

# Anzahl der logischen CPUs
print("Logische CPUs:", psutil.cpu_count(logical=True))

# Anzahl der physischen CPUs
print("Physische CPUs:", psutil.cpu_count(logical=False))
