import xmlrpclib
import random
import time

while True:
	s = xmlrpclib.ServerProxy('http://localhost:8006')
	print "Digite el archivo a  Solicitado ", resource
