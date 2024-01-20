import socket

def main():
    while True:
  
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
        server_address = ('192.168.111.247', 3306)

        try:
            client_socket.connect(server_address)
            print("Connected to the server.")
            while True:
              
                message = input("Enter a message to send (or 'Disconnect' to disconnect): ")
                if message.lower() == "disconnect":
                    client_socket.sendto(message.encode(), server_address)
                    print("Disconnecting from the server.")
                    break

                client_socket.sendto(message.encode(), server_address)
                
                
                response, _ = client_socket.recvfrom(1024)
                print(f"Received response: {response.decode()}")

        except ConnectionRefusedError:
            print("Connection refused. Server may be unavailable.")
        except Exception as e:
            print(f"An error occurred: {e}")

    
        client_socket.close()

        reconnect = input("Do you want to connect again? (yes/no): ")
        if reconnect.lower() != "yes":
            break

if __name__ == "__main__":
    main()
