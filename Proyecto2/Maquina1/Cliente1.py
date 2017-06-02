from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random
import time
import threading
import os

IP = '127.0.0.1'
PUERTO = 9000

Maquinas = ['http://localhost:8002','http://localhost:8003']
##################### CLIENTE ###########################

while True:
	print "\n 1. Leer memoria \n 2. Escribir en memoria \n 3. Cerrar"
	opciones = ['1','2','3']
	opcion = raw_input("Elija una opcion: ")
	if opcion == '1':
		for i in Maquinas:
			maquina = xmlrpclib.ServerProxy(i)
			prestamo = maquina.PrestarPagina()
			if prestamo == 0:
				print "No es posible leer en este momento"
			else:
				print "La memoria tiene capacidad de ", prestamo[2], " lineas"
				print prestamo[0]
		
	if opcion == '2':
		for i in Maquinas:
			maquina = xmlrpclib.ServerProxy(i)
			prestamo = maquina.PrestarPagina()
			if prestamo == 0:
				print "La maquina no tiene memoria disponible"
			else:
				print "La memoria tiene capacidad de ", prestamo[2], " lineas"
				archivo = open(prestamo[1],"w")
				archivo.write(prestamo[0])
				archivo.close()
				os.popen("notepad "+ prestamo[1])
				archivo = open(prestamo[1],"r")
				contenido3 = archivo.read()
				maquina.Consistencia(prestamo[1], contenido3)
				archivo.close()
				os.remove(prestamo[1])

	if opcion == '3':
		break
	if opcion not in opciones:
		print "No existe esta opcion en el menu"