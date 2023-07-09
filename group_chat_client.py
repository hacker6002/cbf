#line 8 

import socket
import threading
import platform

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Use the server IP address
port = 12345  # Use the same port number as the server
client_socket.connect((host, port))

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Error occurred while receiving message.")
            client_socket.close()
            break

def send():
    pc_name = platform.node()  # Get the PC name
    client_socket.send(pc_name.encode())  # Send the PC name to the server

    while True:
        message = input()
        client_socket.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
