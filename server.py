import socket


def serve(debug):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    if debug == True:
        print("Your Computer Name is: " + hostname)
        print("Your Computer IP Address is: " + IPAddr)

    # Define the host and port to listen on
    HOST = '127.0.0.1'  # localhost
    PORT = 12345        # Arbitrary non-privileged port

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((HOST, PORT))
        
        # Listen for incoming connections
        s.listen()

        print(f"Server listening on {HOST}:{PORT}")

        # Accept incoming connections
        conn, addr = s.accept()
        print(f"Connection from {addr} established.")

        # Receive data from the client and send a response
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received message from {addr}: {data.decode()}")
                # Send a response back to the client
                conn.sendall(b"Message received by server.")