import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('192.168.111.247', 3306)
    server_socket.bind(server_address)

    server_socket.listen(5)  # Listen for incoming connections (up to 5 clients in the queue)

    print("Server is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        while True:
            data = client_socket.recv(1024)
            received_message = data.decode()

            if received_message.lower() == "disconnect":
                print(f"Connection with {client_address} closed.")
                client_socket.close()
                break
            else:
                print(f"Received message from {client_address}: {received_message}")

            response_message = input("Enter a message to send: ")
            client_socket.send(response_message.encode())

if __name__ == "__main__":
    main()
