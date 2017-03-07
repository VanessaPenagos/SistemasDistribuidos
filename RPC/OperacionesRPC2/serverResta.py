from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8002),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def resta_function(dato):
	x, y = dato.split("-")
	resta= int(x) - int(y)
	return str(resta)
server.register_function(resta_function, 'res')

# Run the server's main loop
server.serve_forever()


