from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20


# Create server
server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

Archivos = []

class MyFuncs:

        def AgregarArchivo(self):



        def QuitResources(self,resource):
          if resource in Resources:
            r = Resources.index(resource)
            print Resources
            Resources.pop(r)
            return resource
          else:
            print "No esta disponible"
            return 'No esta disponible'
server.register_instance(MyFuncs())

server.serve_forever()
