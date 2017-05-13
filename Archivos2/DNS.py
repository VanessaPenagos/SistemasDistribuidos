from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20

archivosOriginales = ["Dani.txt", "Vane.txt", "Otro.txt"]
clientes = [8007, 8008, 8009]

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:        
    def ActualizarArchivo(self, nombrearchivo, contenidoarchivo, puerto):
        archivo = open(nombrearchivo,"w")
        archivo.write(contenidoarchivo)
        archivo.close()
        if puerto == clientes[0] :
            server1 = xmlrpclib.ServerProxy('http://localhost:'+str(clientes[1]))
        else :
            server1 = xmlrpclib.ServerProxy('http://localhost:'+str(clientes[0]))
        server1.RecibirActualizacion(nombrearchivo, contenidoarchivo)
        return 0

server.register_instance(MyFuncs())

server.serve_forever()
