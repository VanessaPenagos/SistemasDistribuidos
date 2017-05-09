from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from datetime import datetime
import xmlrpclib
import threading
import time
import sys
import random

IP = '127.0.0.1'
PORT = 8005
BUFER_SIZE = 20

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

s = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
s.register_introspection_functions()

class MyFuncs:

s.register_instance(MyFuncs())
t = threading.Thread(target=s.serve_forever)

portlist = [8005,8006,8007]
t.start()
n=0
while True :
    while n<3:
        time.sleep(3)
        try:
        	s1 = xmlrpclib.ServerProxy("http://127.0.0.1:"+str(portlist[n]))
       	except:
       		pass

        n = n+1
    n = 0
sys.exit()
