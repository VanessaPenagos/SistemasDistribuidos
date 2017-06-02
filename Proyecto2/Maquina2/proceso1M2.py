from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import threading
import os

IP = '127.0.0.1'
PUERTO = 9021
Maquinas = ['http://localhost:8001', 'http://localhost:8002']

#------------------------- CLIENTE--------------------------------#

while True:
    print "Proceso de la maquina 2"
    print "\n 1. Leer \n 2. Modificar \n 3. Listar memoria \n 4. Cerrar"
    opciones = ['1', '2', '3', '4']
    opcion = raw_input("Elija una opcion: ")

    if opcion == '1':
        nombre = raw_input("Ingrese el nombre de la pagina ")
        maquina = xmlrpclib.ServerProxy('http://localhost:8002')
        busqueda = maquina.BuscarPagina(nombre)
        if busqueda == 1:
            Archivo = open(nombre, "r")
            contenido = Archivo.read()
            Archivo.close()
            print contenido
        else:
            for i in Maquinas:
                if i != 'http://localhost:8002':
                    maquina = xmlrpclib.ServerProxy(i)
                    Copia = maquina.PedirCopia(nombre)
                    Archivo = open(nombre, "w")
                    Archivo.write(Copia[0])
                    Archivo.close()
                    Archivo = open(nombre, "r")
                    contenido = Archivo.read()
                    Archivo.close()
                    print contenido
