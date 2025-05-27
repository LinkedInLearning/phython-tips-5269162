import tkinter as tk
from tkinter import ttk
import psutil

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖥️ Systemmonitor")
        self.root.geometry("450x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        # Titel
        title = tk.Label(root, text="Systemüberwachung", font=("Helvetica", 18, "bold"),
                         fg="#ffffff", bg="#1e1e2f")
        title.pack(pady=10)

        # Rahmen für Inhalte
        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # Stil anpassen
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TLabel", background="#1e1e2f", foreground="#e0e0e0", font=("Helvetica", 12))

        # Labels
        self.cpu_label = ttk.Label(self.frame, text="CPU-Auslastung:")
        self.cpu_label.grid(row=0, column=0, sticky="w", pady=5)

        self.ram_label = ttk.Label(self.frame, text="RAM-Nutzung:")
        self.ram_label.grid(row=1, column=0, sticky="w", pady=5)

        self.disk_label = ttk.Label(self.frame, text="Festplattennutzung:")
        self.disk_label.grid(row=2, column=0, sticky="w", pady=5)

        self.net_label = ttk.Label(self.frame, text="Netzwerkverkehr:")
        self.net_label.grid(row=3, column=0, sticky="w", pady=5)

        self.update_loop()

    def update_loop(self):
        # CPU
        cpu = psutil.cpu_percent()
        self.cpu_label.config(text=f"🧠 CPU-Auslastung: {cpu:.1f}%")

        # RAM
        ram = psutil.virtual_memory()
        self.ram_label.config(
            text=f"💾 RAM: {ram.percent:.1f}% ({ram.used // (1024**2)} MB von {ram.total // (1024**2)} MB)")

        # Festplatte
        disk = psutil.disk_usage('/')
        self.disk_label.config(
            text=f"📀 Festplatte: {disk.percent:.1f}% ({disk.used // (1024**3)} GB von {disk.total // (1024**3)} GB)")

        # Netzwerk
        net = psutil.net_io_counters()
        sent = net.bytes_sent // (1024**2)
        recv = net.bytes_recv // (1024**2)
        self.net_label.config(text=f"🌐 Netzwerk: ⬆ {sent} MB | ⬇ {recv} MB")

        # alle 1 Sekunde aktualisieren
        self.root.after(1000, self.update_loop)

def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
