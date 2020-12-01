import socket
from threading import *
import time
import random
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 50003
print(host)
print(port)
serversocket.bind((host, port))
position = random.randint(-10, 10)


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.position = str(random.randint(-10, 10))
        self.start()

    def run(self):
        while 1:
            self.sock.send(self.position.encode())
            data = self.sock.recv(1024)
            data_arr = pickle.loads(data)
            if data_arr[1] == 50:
                self.position = int(self.position) + 3
            if data_arr[1] == -50:
                self.position = int(self.position) - 3
            if data_arr[1] == 5:
                self.position = int(self.position) + random.randint(-7, 7)

            #self.position = self.position + random.randint(-3, 3)
            print('Current position = ', self.position)
            self.position = str(self.position)
            time.sleep(0.5)
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

