import socket
import random
import time

HOST = '0.0.0.0'  # damit Clients im Netzwerk Server erreichen können
PORT = 5025         # Beliebiger freier Port für die SPS-Simulation

def start_mock_sps():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Mock SPS läuft auf {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Verbindung von {addr} erhalten.")

        while True:
            motor_speed = random.randint(0, 100)  # Simulierter Wert
            data = f"{motor_speed}\n"
            conn.sendall(data.encode())  # Senden des Werts als String
            
            time.sleep(2)  # Simuliert Echtzeit-Datenübertragung

        conn.close()

if __name__ == "__main__":
    start_mock_sps()
