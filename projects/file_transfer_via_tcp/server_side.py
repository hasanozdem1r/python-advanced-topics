import socket
from threading import Thread
from socketserver import ThreadingMixIn

TCP_IP = "localhost"
TCP_PORT = 9001
BUFFER_SIZE = 1024


# inheritance
class ClientThread(Thread):

    # class constructor
    def __init__(self, ip, port, sock):
        # inheritance of Thread class
        Thread.__init__(self)
        self.ip = ip
        self.sock = sock
        self.port = port
        print(f"New thread started for {ip} at {port}")

    # inherited method from Thread class
    def run(self) -> None:
        f_name = "my_text2.txt"
        f_obj = open(f_name, "rb")
        while True:
            line = f_obj.read(BUFFER_SIZE)
            while line:
                self.sock.send(line)
                print(f"Sent {repr(line)}")
                line = f_obj.read(BUFFER_SIZE)
            if not line:
                f_obj.close()
                self.sock.close()
                break


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcp_socket.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcp_socket.listen(5)
    print("Waiting for incoming connections ...")
    (connection, (ip, port)) = tcp_socket.accept()
    print(f"Got connection from {ip} - {port}")
    new_thr = ClientThread(ip, port, connection)
    new_thr.start()
    threads.append(new_thr)
