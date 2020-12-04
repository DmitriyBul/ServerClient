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
        self.position = str(random.randint(-15, 15))
        self.start()

    def run(self):
        print('Current position = ', self.position)
        while 1:
            self.sock.send(self.position.encode())
            data = self.sock.recv(1024)
            data_arr = pickle.loads(data)
            if data_arr[1] == 30:
                self.position = int(self.position) + 3
                print('Current position = ', self.position)
            if data_arr[1] == -30:
                self.position = int(self.position) - 3
                print('Current position = ', self.position)
            if data_arr[1] == 60:
                self.position = int(self.position) + 6
                print('Current position = ', self.position)
            if data_arr[1] == -60:
                self.position = int(self.position) - 6
                print('Current position = ', self.position)
            if data_arr[1] == 100:
                self.position = int(self.position) + 10
                print('Current position = ', self.position)
            if data_arr[1] == -100:
                self.position = int(self.position) - 10
                print('Current position = ', self.position)
            if data_arr[0] == 50:
                self.position = int(self.position) + random.randint(-14, 14)
                print('Current position = ', self.position)
            if data_arr[3] > 14:
                print('Mission complete!')
                self.position = 500
                self.sock.send(str(self.position).encode())
                break
            if data_arr[2] == 1:
                print('Robot is dead')
                break
            #self.position = self.position + random.randint(-3, 3)

            self.position = str(self.position)
            time.sleep(0.1)
            #data = int(data) + 2
            #self.sock.send(str(data).encode())

serversocket.listen(5)
print('Server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)




