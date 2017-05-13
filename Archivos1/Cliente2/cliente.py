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

#################### SERVIDOR ###########################

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PUERTO),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
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
        print "Abriendo archivo..."
        os.popen("notepad "+ "Vane.txt")
        archivo = open("Vane.txt","r")
        contenido = archivo.read()
        server.ActualizarArchivo("Vane.txt", contenido)
        archivo.close()

    if opcion == '2' :
        print "Abriendo archivo..."
        os.popen("notepad "+ "Dani.txt")
        archivo = open("Dani.txt","r")
        contenido = archivo.read()
        server.ActualizarArchivo("Dani.txt", contenido)
        archivo.close()

    if opcion == '3' :
        print "Abriendo archivo..."
        os.popen("notepad "+ "Otro.txt")
        archivo = open("Otro.txt","r")
        contenido = archivo.read()
        server.ActualizarArchivo("Otro.txt", contenido)
        archivo.close()

    if opcion not in opciones:
        print "No existe esta opcion en el menu"
