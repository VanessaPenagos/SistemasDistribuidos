#!/usr/bin/env python
import socket

Dato1 = "35" # number 1
Dato2 = "50" # number 2

s = socket.socket()
s.connect(('localhost', 9999))
s.send(Dato1)
dato = s.recv(1024)
s.send(Dato2)
dato = s.recv(1024)
s.close()
print "Se enviaron los numeros : "
print Dato1 , Dato2
print "La suma de los datos es : ", dato
