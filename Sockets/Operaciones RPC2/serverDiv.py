from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8004),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def division_function(dato):
	x, y = dato.split("/")
	div= int(x) / int(y)
	return str(div)
server.register_function(division_function, 'div')

# Run the server's main loop
server.serve_forever()

