#!/usr/bin/env python
import socket

Datos = ["35" , "50" ]

s = socket.socket()
s.connect(('localhost', 9999))
s.send(Datos[0])
dato = s.recv(1024)
s.send(Datos[1])
dato = s.recv(1024)
s.close()
print "Se enviaron los numeros :", Datos[0] , Datos[1]
print "La suma de los datos es :", dato
