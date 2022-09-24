import socket

TCP_IP = "localhost"
TCP_PORT = 9001
BUFFER_SIZE = 1024

s_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_obj.connect((TCP_IP, TCP_PORT))

# context manager __enter__ , __exit__
with open("received_file2.txt", "wb") as file_obj:
    print("File opened")
    while True:
        print("Receiving data ...")
        data = s_obj.recv(BUFFER_SIZE)
        print("data=%s", (data))
        if not data:
            print("File close")
            break
        # writing data to a file
        file_obj.write(data)

print("Successfully get the file")
s_obj.close()
print("Connection closed")
