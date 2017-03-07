import socket
import time

Mensaje = "Dame la hora actual"

while True :
    s = socket.socket()
    s.connect(('localhost', 9999))
    time.sleep(2)
    s.send(Mensaje)
    print Mensaje
    hora = s.recv(1024)
    s.close()
    print "La hora es :", hora
