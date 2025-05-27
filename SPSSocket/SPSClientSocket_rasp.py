import socket

HOST = '192.168.13.246'  
PORT = 5025         

def read_motor_speed():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        data = client_socket.recv(1024).decode().strip()  # Daten empfangen und bereinigen
        if not data:
            break  # Verbindung verloren
        motor_speed = int(data)
        
        if motor_speed > 50:
            print(f"Motor läuft mit hoher Geschwindigkeit! ({motor_speed})")
        else:
            print(f"Motor läuft mit niedriger Geschwindigkeit. ({motor_speed})")

    client_socket.close()

if __name__ == "__main__":
    read_motor_speed()
