from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import threading
import os

IP = '127.0.0.1'
PUERTO = 8001
Paginas = {"M1P1.txt": 8}
CapacidadTotal = {"M1P1.txt": 8}
Disponibilidad = [0, 0]


#---------------------------Servidor-------------------------------#
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2', )


server = SimpleXMLRPCServer((IP, PUERTO), requestHandler=RequestHandler)
server.register_introspection_functions()


class MyFuncs:
    def ActualizarPagina(self, nombre, contenido):
        if nombre in Paginas:
            lineas = len(open(nombre).readlines())
            Pos = Paginas.index(nombre)
            if lineas > Paginas[nombre]:
                return 0
            else:
                pagina = open(nombre, "w")
                pagina.write(contenido)
                pagina.close()
                Paginas[nombre] -= lineas
                return 1
        else:
            return -1

    def AgregarCopia(self, nombre, capacidad):
        Paginas[nombre] = capacidad
        return "Copia agregada"

    def BuscarPagina(self, nombre):
        if nombre in Paginas:
            print "El nombre es : ", nombre
            return Paginas[nombre], CapacidadTotal[nombre]
        else:
            return -1

    def PedirCopia(self, nombre):
        if nombre in Paginas:
            capacidad = Paginas[nombre]
            Archivo = open(nombre, "r")
            contenido = Archivo.read()
            Archivo.close()
            return contenido, capacidad, CapacidadTotal[nombre]
        else:
            return -1

    def Bloqueo(self, nombre):
        Pos = nombre[1]
        Disponibilidad[Pos] = 1
        return 1

    def Desbloqueo(self, nombre):
        Pos = nombre[1]
        Disponibilidad[Pos] = 0
        return 0


server.register_instance(MyFuncs())
server.serve_forever()
