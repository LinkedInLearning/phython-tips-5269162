import psutil
import time
print("Live-Systemmonitor in der Konsole")
while True:
    print("CPU:", psutil.cpu_percent(), "%")
    print("RAM:", psutil.virtual_memory().percent, "%")
    time.sleep(1)