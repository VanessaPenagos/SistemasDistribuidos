import socket
import time


while True :
    s = socket.socket()
    s.connect(('localhost', 9002))
    peticion = s.recv(1024)
    s.send(time.strftime("%H:%M:%S"))
    horan=s.recv(1024)
    print horan

    s.close()

