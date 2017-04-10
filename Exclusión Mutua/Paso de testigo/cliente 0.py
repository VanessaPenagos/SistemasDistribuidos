
import socket
import random
import time 

portCliente0 = 9000

#Se crea el socket
s0 = socket.socket()
s0.connect(('localhost',9001))
s0.send('1')
s0.close()

s = socket.socket()
s.bind(('localhost' , portCliente0))
s.listen(1)   

print "Inicia Conexion" 

while True:

	conexion, clienteDireccion = s.accept()

	token = conexion.recv(1024)
	print token
	r = random.randint(0,1)
	if r == 0:
		s1 = socket.socket()
		s1.connect(('localhost',9001))
		s1.send('1')
		s1.close()
	else:
		print "Usando recursos"
		time.sleep(2)
		s1 = socket.socket()
		s1.connect(('localhost',9001))
		s1.send('1')
		s1.close()
s.close()
