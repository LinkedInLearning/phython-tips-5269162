from paramiko import SSHClient
from scp import SCPClient
import paramiko

# Verbindungskonfiguration
hostname = '192.168.13.246'     # IP-Adresse oder Hostname des Servers
port = 22                    # Standard-SSH-Port
username = 'trillian'
password = 'HerzAusGold'   # Alternativ: nutzen Key-basierte Authentifizierung


# SSH-Verbindung aufbauen
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port=port, username=username, password=password)

# SCP-Client erstellen
with SCPClient(ssh.get_transport()) as scp:
    # Datei hochladen
    scp.put('kultur.txt', '/home/trillian')

    # Datei herunterladen
    scp.get('kultur.txt', 'erlk2.txt')

ssh.close()

