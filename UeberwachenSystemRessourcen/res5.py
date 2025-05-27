import psutil

# Alle laufenden Prozesse auflisten
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)

# Einen bestimmten Prozess analysieren
try:
    p = psutil.Process(27500)  # z. B. mit PID 1234
    print("Name:", p.name())
    print("Status:", p.status())
    print("CPU-Zeit:", p.cpu_times())
    print("Speicherverbrauch:", p.memory_info())
except:
    print("Prozess nicht vorhanden")