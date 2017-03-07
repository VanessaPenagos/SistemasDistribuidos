from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def leerArchivo(dato):
    archivo = open(dato, "r")
    contenido = archivo.read()
    return contenido
server.register_function(leerArchivo, 'text')

# Run the server's main loop
server.serve_forever()
