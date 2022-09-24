from socket import *

host_name = "localhost"
host_port = 12345
# socket(socket_family,socket_type)
host_socket = socket(AF_INET, SOCK_DGRAM)
# connect socket to host from given port
host_socket.bind((host_name, host_port))
print("Host ready to retrieve data")
while True:
    # recvfrom(port_name) receive msgs from given port
    message, client_address = host_socket.recvfrom(4096)
    print("Message received from client", message)
    new_msg = message.upper()
    host_socket.sendto(new_msg, client_address)
    print("Message sent back to client")
    if message == b"axson":
        break
print("Close message received. Host is closing")
host_socket.close()
print("Host closed")
