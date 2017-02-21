import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
print s.text("nombrearchivo.txt")

# Print list of available methods
#print s.system.listMethods()
