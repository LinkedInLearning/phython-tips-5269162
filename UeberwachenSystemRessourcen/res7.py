import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Systemmonitor")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.cpu_label = ttk.Label(root, text="CPU-Auslastung: ", font=('Arial', 12))
        self.cpu_label.pack(pady=5)

        self.ram_label = ttk.Label(root, text="RAM-Auslastung: ", font=('Arial', 12))
        self.ram_label.pack(pady=5)

        self.disk_label = ttk.Label(root, text="Festplattennutzung: ", font=('Arial', 12))
        self.disk_label.pack(pady=5)

        self.net_label = ttk.Label(root, text="Netzwerk: ", font=('Arial', 12))
        self.net_label.pack(pady=5)

        self.update_loop()

    def update_loop(self):
        # CPU
        cpu = psutil.cpu_percent()
        self.cpu_label.config(text=f"CPU-Auslastung: {cpu:.1f}%")

        # RAM
        ram = psutil.virtual_memory()
        self.ram_label.config(text=f"RAM: {ram.percent:.1f}% ({ram.used // (1024**2)} MB von {ram.total // (1024**2)} MB)")

        # Disk
        disk = psutil.disk_usage('/')
        self.disk_label.config(text=f"Festplatte: {disk.percent:.1f}% ({disk.used // (1024**3)} GB von {disk.total // (1024**3)} GB)")

        # Netzwerk
        net = psutil.net_io_counters()
        sent = net.bytes_sent // (1024**2)
        recv = net.bytes_recv // (1024**2)
        self.net_label.config(text=f"Netzwerk: ⬆ {sent} MB | ⬇ {recv} MB")

        self.root.after(1000, self.update_loop)  # alle 1 Sekunde aktualisieren

def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
