# async.py

import socket
import threading
import SocketServer

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message))
        response = str(sock.recv(1024))
        print("Received: {}".format(response))
    finally:
        sock.close()

if __name__ == "__main__":
    # port 0 means to select an arbitrary unused port
    #HOST, PORT = "localhost", 0
    HOST, PORT = "localhost", 10000


    #ip, port = server.server_address
    ip, port = HOST, PORT

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
