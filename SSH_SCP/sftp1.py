import paramiko

# Verbindungskonfiguration
hostname = '192.168.13.246'     # IP-Adresse oder Hostname des Servers
port = 22                    # Standard-SSH-Port
username = 'trillian'
password = 'HerzAusGold'   # Alternativ: nutzen Key-basierte Authentifizierung

transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# Datei hochladen
sftp.put('kultur.txt', 'kultur.txt')

# Datei herunterladen
sftp.get('kultur.txt', 'erlk.txt')

sftp.close()
transport.close()
