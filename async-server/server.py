# async.py

import socket
import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024))
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data))
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # port 0 means to select an arbitrary unused port
    #HOST, PORT = "localhost", 0
    HOST, PORT = "localhost", 10000

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # start a thread with the server. 
    # the thread will then start one more thread for each request.
    server_thread = threading.Thread(target=server.serve_forever)

    # exit the server thread when the main thread terminates
    #server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    #server.shutdown()
