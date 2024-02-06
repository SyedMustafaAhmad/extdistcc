import socket


def wait(debug):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    if debug == True:
        print("Your Computer Name is: " + hostname)
        print("Your Computer IP Address is: " + IPAddr)

    # Define the server address and port
    SERVER_HOST = '127.0.0.1'  # localhost
    SERVER_PORT = 12345        # Same port as the server

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((SERVER_HOST, SERVER_PORT))

        # Send a message to the server
        message = "Hello, server!"
        s.sendall(message.encode())
        print(f"Message sent to server: {message}")

        # Receive a response from the server
        data = s.recv(1024)
        print(f"Response from server: {data.decode()}")