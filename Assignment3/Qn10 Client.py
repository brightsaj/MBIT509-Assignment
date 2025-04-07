import socket


def start_client(host, port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Receive a message from the server
        message = client_socket.recv(1024).decode()
        print("Message received from server:", message)
    except socket.error as e:
        print(f"Error during connection or communication: {e}")
    finally:
        # Close the client socket
        client_socket.close()


if __name__ == "__main__":
    # Connect to the server at localhost (127.0.0.1) and port 65432
    start_client('127.0.0.1', 65432)