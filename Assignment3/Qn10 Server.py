import socket


def start_server(host, port):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")
    except socket.error as e:
        print(f"Error binding socket: {e}")
        return

    # Wait for a client connection
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Send a message to the client
        message = "Hello from server!"
        client_socket.sendall(message.encode())
        print("Message sent to client.")

        # Close the client connection
        client_socket.close()
    except socket.error as e:
        print(f"Error during communication: {e}")
    finally:
        # Close the server socket
        server_socket.close()


if __name__ == "__main__":
    # Start the server on localhost (127.0.0.1) and port 65432
    start_server('127.0.0.1', 65432)