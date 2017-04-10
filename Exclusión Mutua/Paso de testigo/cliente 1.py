
import socket
import random
import time 

portCliente1 = 9001

#Se crea el socket
s = socket.socket()
s.bind(('localhost' , portCliente1))
s.listen(1)  
 
print "Inicia Conexion" 

while True:

    conexion, clienteDireccion = s.accept()

    token = conexion.recv(1024)
    print token
    r = random.randint(0,1)
    if r == 0:
        s1 = socket.socket()
        s1.connect(('localhost',9002))
        s1.send('2')
        s1.close()
    else:
        print "Usando recursos"
        time.sleep(2)
        s1 = socket.socket()
        s1.connect(('localhost',9002))
        s1.send('2')
    s1.close()
s.close()