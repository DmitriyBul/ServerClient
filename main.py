import socket
from threading import *
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 50003
print(host)
print(port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            self.sock.send('-5'.encode())
            data = self.sock.recv(1024).decode()
            print('Client sent:', data)
            time.sleep(5)
            #data = int(data) + 2
            #self.sock.send(str(data).encode())

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)









    '''
    data = conn.recv(4096)
    if not data: break
    conn.send(data)
conn.close()
'''

