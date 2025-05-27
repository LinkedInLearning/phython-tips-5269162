import paramiko

# Verbindungskonfiguration
hostname = '192.168.13.246'     # IP-Adresse oder Hostname des Servers
port = 22                    # Standard-SSH-Port
username = 'trillian'
password = 'HerzAusGold'   # Alternativ: nutzen Key-basierte Authentifizierung

# SSH-Client erstellen
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Verbindung aufbauen
    client.connect(hostname=hostname, port=port, username=username, password=password)

    # Befehl auf dem Server ausführen
    stdin, stdout, stderr = client.exec_command('ls -la')

    # Ausgabe lesen
    print("Ausgabe:")
    for line in stdout:
        print(line.strip())

    # Fehlerausgabe (falls vorhanden)
    err = stderr.read().decode()
    if err:
        print("Fehler:", err)

finally:
    # Verbindung schließen
    client.close()
