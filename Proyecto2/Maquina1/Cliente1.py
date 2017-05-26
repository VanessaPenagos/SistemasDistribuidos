from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random
import time
import threading
import os

IP = '127.0.0.1'
PUERTO = 8008
##################### CLIENTE ###########################

while True:
	print "\n 1. Listar mis paginas \n 2. Listar todas las paginas \n 3. Leer Archivo \n 4. Modificar Archivos\n 5. Eliminar archivos \n 6. Cerrar"
	opciones = ['1','2','3','4','5']
	opcion = raw_input("Elija una opcion: ")
	if opcion == '1':
		i = 1 
		print "Mis paginas son:"
		server = xmlrpclib.ServerProxy('http://localhost:8007')
		paginas = server.ListarPagina()
		for elemento in paginas:
			print str(i) + ". " + elemento
			i += 1
	if opcion == '2':
		server_controlador = xmlrpclib.ServerProxy('http://localhost:8006')
		paginas = server_controlador.ListarPaginas()
		i = 1
		print "Los archivos disponibles son: "
		for elemento in archivos:
			print str(i) + ". " + elemento
			i += 1
	if opcion == '3':
		nombre = raw_input("Ingrese el nombre del archivo (con su extension): ")
		mi_direccion=IP+":"+str(PUERTO)
		direccion, permiso = server.BuscarArchivo(nombre, mi_direccion)
		if direccion == "Nope":
			print "No se encuentra el archivo o el archivo se encuentra en uso"
		else:
			maquinaN = xmlrpclib.ServerProxy(direccion)
			contenido1 = maquinaN.LeerArchivo(nombre)
			print "\n",contenido1
	if opcion == '4':
		nombre = raw_input("Ingrese el nombre del archivo (con su extension): ")
		mi_direccion=IP+":"+str(PUERTO)
		direccion, permiso = server.BuscarArchivo(nombre, mi_direccion)
		if direccion == "Nope":
			print "No se encuentra el archivo o el archivo se encuentra en uso"
		else:
			if permiso == 1:
				server.Bloqueo(nombre)
				maquinaN = xmlrpclib.ServerProxy(direccion)
				contenido2 = maquinaN.LeerArchivo(nombre)
				archivo = open(nombre,"w")
				archivo.write(contenido2)
				archivo.close()
				os.popen("notepad "+ nombre)
				archivo = open(nombre,"r")
				contenido3 = archivo.read()
				maquinaN.ActualizarArchivo(nombre, contenido3)
				archivo.close()
				if nombre not in MisArchivos:
					os.remove(nombre)
				server.Desbloqueo(nombre)
			else:
				print "No tiene permiso para escribir el archivo"			
	if opcion == '5':
		nombre = raw_input("Ingrese el nombre del archivo (con su extension): ")
		mi_direccion=IP+":"+str(PUERTO)
		direccion, permiso = server.BuscarArchivo(nombre, mi_direccion)
		if direccion == "Nope":
			print "No se encuentra el archivo o el archivo se encuentra en uso"
		else:
			if permiso == 1:
				maquinaN = xmlrpclib.ServerProxy(direccion)
				maquinaN.EliminarArchivos(nombre)
				server.EliminarArchivos(nombre)
				if nombre in MisArchivos:
					MisArchivos.remove(nombre)		
					os.remove(nombre)
			else:
				print "No tiene permisos para eliminar el archivo"
	if opcion == '6':
		break
	if opcion not in opciones:
		print "No existe esta opcion en el menu"