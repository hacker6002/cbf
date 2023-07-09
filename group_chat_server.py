#line 32
import socket
import threading

def client_thread(client_socket, address):
    pc_name = client_socket.recv(1024).decode()  # Receive the PC name from the client
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received from {pc_name} ({address[0]}): {message}")
                broadcast(f"{pc_name}: {message}", client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Use your server IP address
port = 12345  # Choose a port number
server_socket.bind((host, port))
server_socket.listen(3)

clients = []
while True:
    client_socket, address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connected with {address}")
    threading.Thread(target=client_thread, args=(client_socket, address)).start()
