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

Resources = ['1','2','3','4','5','6']
print "Esperando a que sirva"

class MyFuncs:

        def QuitResources(self,resource):
          if resource in Resources:
            r = Resources.index(resource)
            print "Muerto"
            print Resources
            Resources.pop(r)
            return resource
          else:
            print "No esta disponible"
            return 'No esta disponible'
        def AddResources(self,resource):
          if resource in Resources:
            print "Nope!"
            return "El recurso ya se ha devuelto"
          else:
            print "Agregando"
            Resources.append(resource)
            print Resources
            return 0
server.register_instance(MyFuncs())

server.serve_forever()
