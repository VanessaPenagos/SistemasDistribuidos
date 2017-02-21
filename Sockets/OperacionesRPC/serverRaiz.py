from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8006),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def raiz_function(dato):
	x, y = dato.split("r")
	raiz= pow( int(x) , (1.0 / int(y)))
	return str(raiz)
server.register_function(raiz_function, 'raiz')

# Run the server's main loop
server.serve_forever()

