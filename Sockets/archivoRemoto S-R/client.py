#!/usr/bin/env python
import socket

s = socket.socket()
s.connect(('localhost', 9999))
s.send("valentinap.txt")
texto = s.recv(1024)
s.close()
print texto
