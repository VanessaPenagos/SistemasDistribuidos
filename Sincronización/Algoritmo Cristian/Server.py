import urllib2
from datetime import datetime
import socket
import time

def getOnlineUTCTime():
    time.sleep(3)
    webpage = urllib2.urlopen("http://just-the-time.appspot.com/")
    internettime = webpage.read()
    OnlineUTCTime = str(datetime.strptime(internettime.strip(), '%Y-%m-%d %H:%M:%S'))
    date, hour = OnlineUTCTime.split(" ")
    H, M, S = hour.split(":")
    H = int(H)-5
    if (H < 0):
        H = 24 + H
    hour = str(H)+":"+M+":"+S
    return hour


s = socket.socket()
s.bind(('localhost' , 9999))

s.listen(5)
print "Esperando conexion"
while True:
    conexion, clienteDireccion = s.accept()
    dato = conexion.recv(1024)
    Hora = getOnlineUTCTime()
    print "Dato enviado", Hora
    conexion.send(Hora)
    conexion.close()
