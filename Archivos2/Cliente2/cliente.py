from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random
import time
import threading
import os

IP = '127.0.0.1'
PUERTO = 8007
CopiaArchivos = ["Dani.txt", "Vane.txt", "Otro.txt"]
OtrosClientes = [8008, 8009]
#################### SERVIDOR ###########################

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PUERTO),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:

    def Permiso(self):
        w = random.randint(0,1)
        r = random.randint(0,1)
        return (r,w)

    def RecibirActualizacion(self, nombrearchivo, contenidoarchivo):
        archivo = open(nombrearchivo,"w")
        archivo.write(contenidoarchivo)
        archivo.close()
        return 0

server.register_instance(MyFuncs())

t = threading.Thread(target=server.serve_forever)
t.start()

##################### CLIENTE ###########################

server = xmlrpclib.ServerProxy('http://localhost:8006')

while True:
    print "\n 1. Vane.txt \n 2. Dani.txt \n 3. Otro.txt \n"
    opciones = ['1','2','3']
    opcion = raw_input("Elija una opcion: ")

    if opcion == '1' :
        server1 = xmlrpclib.ServerProxy('http://localhost:8008')
        server2 = xmlrpclib.ServerProxy('http://localhost:8009')
        permisos1 = server1.Permiso()
        permisos2 = server2.Permiso()
        print "Permisos", permisos1[1], " ", permisos2[1]
        if (permisos1[1] + permisos2[1] + 1) >= 2 :
            print "Abriendo archivo..."
            os.popen("notepad "+ "Vane.txt")
            archivo = open("Vane.txt","r")
            contenido = archivo.read()
            server.ActualizarArchivo("Vane.txt", contenido, PUERTO)
            archivo.close()
        else :
            print "No tiene permisos para esta accion"

    if opcion == '2' :
        server1 = xmlrpclib.ServerProxy('http://localhost:8008')
        server2 = xmlrpclib.ServerProxy('http://localhost:8009')
        permisos1 = server1.Permiso()
        permisos2 = server2.Permiso()
        print "Permisos", permisos1[1], " ", permisos2[1]
        if (permisos1[1] + permisos2[1] + 1) >= 2 :
            print "Abriendo archivo..."
            os.popen("notepad "+ "Dani.txt")
            archivo = open("Dani.txt","r")
            contenido = archivo.read()
            server.ActualizarArchivo("Dani.txt", contenido, PUERTO)
            archivo.close()
        else :
            print "No tiene permisos para esta accion"

    if opcion == '3' :
        server1 = xmlrpclib.ServerProxy('http://localhost:8008')
        server2 = xmlrpclib.ServerProxy('http://localhost:8009')
        permisos1 = server1.Permiso()
        permisos2 = server2.Permiso()
        print "Permisos", permisos1[1], " ", permisos2[1]
        if (permisos1[1] + permisos2[1] + 1) >= 2 :
            print "Abriendo archivo..."
            os.popen("notepad "+ "Otro.txt")
            archivo = open("Otro.txt","r")
            contenido = archivo.read()
            server.ActualizarArchivo("Otro.txt", contenido,PUERTO)
            archivo.close()
        else :
            print "No tiene permisos para esta accion"

    if opcion not in opciones:
        print "No existe esta opcion en el menu"
