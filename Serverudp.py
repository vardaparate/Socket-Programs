import socket

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('192.168.111.247', 3306)
    server_socket.bind(server_address)
    
    print("Server is listening...")

    while True:
        try:
            data, client_address = server_socket.recvfrom(1024)
            received_message = data.decode()

            if received_message.lower() == "disconnect":
              print(f"Connection with {client_address} closed.")
            else:
              print(f"Received message from {client_address}: {received_message}")
         
            if received_message.lower() == "disconnect":
              response_message = "Disconnecting..."
            else:
              response_message = input("Enter a message to send: ")
              server_socket.sendto(response_message.encode(), client_address)
            #response_message = "Message received!"


            

        except ConnectionResetError:
            print("Connection with the remote host was forcibly closed.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
