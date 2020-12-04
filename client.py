import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 50003
s.connect((host, port))
lst = [0, 0, 0, 0]


def power_calc():

   position = s.recv(1024).decode()
   lst[0] = 0
   if int(position) >= -3 and int(position) <= 3:
      lst[0] = 50
      lst[1] = 10
      data_string = pickle.dumps(lst)
      s.send(data_string)
      lst[3] = lst[3] + 1
      print(lst[0])
   if int(position) > -5 and int(position) < -3:
      lst[1] = 30
      data_string = pickle.dumps(lst)
      s.send(data_string)
      print(lst[1])
   if int(position) > 3 and int(position) < 5:
      lst[1] = -30
      data_string = pickle.dumps(lst)
      s.send(data_string)
      print(lst[1])
   if int(position) > -10 and int(position) <= -5:
      lst[1] = 60
      data_string = pickle.dumps(lst)
      s.send(data_string)
      print(lst[1])
   if int(position) >= 5 and int(position) < 10:
      lst[1] = -60
      data_string = pickle.dumps(lst)
      s.send(data_string)
      print(lst[1])
   if int(position) > -15 and int(position) <= -10:
      lst[1] = 100
      data_string = pickle.dumps(lst)
      s.send(data_string)
      print(lst[1])
   if int(position) >= 10 and int(position) < 15:
      lst[1] = -100
      data_string = pickle.dumps(lst)
      s.send(data_string)
      print(lst[1])
   if (int(position) >= 15 and int(position) != 500) or int(position) <= -15:
      lst[1] = 0
      lst[2] = 1
      print('Robot is dead')
      data_string = pickle.dumps(lst)
      s.send(data_string)

   if int(position) == 500:
      print('Mission complete!')


while True:
   power_calc()

s.close ()
