import psutil

# Netzwerk-I/O
net = psutil.net_io_counters()
print(f"Bytes gesendet: {net.bytes_sent / (1024**2):.2f} MB")
print(f"Bytes empfangen: {net.bytes_recv / (1024**2):.2f} MB")

# Netzwerkverbindungen
for conn in psutil.net_connections(kind='inet'):
    print(f"PID: {conn.pid}, Status: {conn.status}, Lokale Adresse: {conn.laddr}, Entfernte Adresse: {conn.raddr}")
