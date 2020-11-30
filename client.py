import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 50003
s.connect((host, port))

def ts():
   data = s.recv(1024).decode()
   new_data = int(data) + 2
   s.send(str(new_data).encode())


while True:
   ts()


s.close ()
'''
arr = ([1,2,3,4,5,6],[1,2,3,4,5,6])
data_string = pickle.dumps(arr)
client.send(data_string)

data = client.recv(4096)
data_arr = pickle.loads(data)
client.close()
print ('Received', repr(data_arr))

'''
