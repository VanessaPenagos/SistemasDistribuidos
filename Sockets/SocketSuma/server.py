#Cliente - servidor
#Sockets
#Se reciben dos numeros y se devuelve la suma de estos

import socket

#Se crea el socket
s = socket.socket()
s.bind(('localhost' , 9999))
Total = 0

#Para Escuchar conexiones
s.listen(1)   #Escuchar conexiones ( 1 maximo)
print "Esperando conexion"
conexion, clienteDireccion = s.accept()

while True:
    dato = conexion.recv(1024)
    if not dato: break
    Total += int(dato)
    print "Dato recibido  :D"
    conexion.send(str(Total))  # echo
conexion.close()
