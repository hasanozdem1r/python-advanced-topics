from socket import *

host_name = "localhost"
host_port = 12345
# socket(socket_family,socket_type)
client_socket = socket(AF_INET, SOCK_DGRAM)
# connect socket to host from given port
while True:
    message = input("Enter your message:")
    client_socket.sendto(bytes(message, encoding="utf-8"), (host_name, host_port))
    new_msg, host_address = client_socket.recvfrom(4096)
    print(new_msg)
    if new_msg == b"AXSON":
        break
client_socket.close()
print("Client socket closed!")
