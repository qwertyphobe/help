import socket

def start_server_TCP():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")

    data = conn.recv(1024).decode()
    print(f"Received from client: {data}")

    response = "Hello from server!"
    conn.send(response.encode())

    conn.close()
    print("Server connection closed.")

if __name__ == "__main__":
    start_server_TCP()


import socket

def start_client_TCP():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = "Hello from client!"
    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")

    client_socket.close()
    print("Client connection closed.")

if __name__ == "__main__":
    start_client_TCP()


import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP server is listening on port 12345...")

    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from client: {data.decode()}")

    response = "Hello from UDP server!"
    server_socket.sendto(response.encode(), client_address)

    print("Response sent to client")
    print("Server connection closed.")

if __name__ == "__main__":
    start_udp_server()


import socket

def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #prepare message
    message = "Hello from UDP client!"
    client_socket.sendto(message.encode(), ('localhost', 12345))

    # Receive response from server
    data, server_address = client_socket.recvfrom(1024)  # Buffer size
    print(f"Received from server: {data.decode()}")

    client_socket.close()
    print("Client connection closed.")

if __name__ == "__main__":
    start_udp_client()
