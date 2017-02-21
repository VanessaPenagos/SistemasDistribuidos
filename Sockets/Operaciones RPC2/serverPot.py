from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8005),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def potencia_function(dato):
	x, y = dato.split("^")
	pot= pow(int(x),int(y))
	return str(pot)
server.register_function(potencia_function, 'pot')

# Run the server's main loop
server.serve_forever()

