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

    archivo = open(dato, "r")
    contenido = archivo.read()
    conexion.send(contenido)  # echo
conexion.close()
