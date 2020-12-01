import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 50003
s.connect((host, port))
lst = [0, 0]


def ts():
   position = s.recv(1024).decode()

   if int(position) >= -3 and int(position) <= 3:
      lst[1] = 5
      data_string = pickle.dumps(lst)
      s.send(data_string)

   if int(position) > -10 and int(position) < -3:
      lst[1] = 50
      data_string = pickle.dumps(lst)
      s.send(data_string)
   if int(position) > 3 and int(position) < 10:
      lst[1] = -50
      data_string = pickle.dumps(lst)
      s.send(data_string)
   print(lst[1])
   '''
   else:
      lst[1] = 5
      data_string = pickle.dumps(lst)
      s.send(data_string)
'''
   #new_data = int(data) + 2
   #s.send(str(new_data).encode())


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
