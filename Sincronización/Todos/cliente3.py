from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from datetime import datetime
import xmlrpclib
import threading
import time
import sys


def CPromedio(horas):
    a = 0
    for i in range(len(horas)):
        a = a + horas[i]
    a = a/len(horas)
    return a 

def SecondstoUTC(seconds):
	H = seconds/3600
	M = (seconds - H*3600) /60
	S = seconds - H*3600 - M*60;
	Hora = str(H)+":"+str(M)+":"+str(S)
	return Hora

def UTCtoSeconds(hour):
   H, M, S = hour.split(":")
   Seconds  = ( (int(M) * 60) + (int(H) * 3600) + int(S) )
   return Seconds


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

IP = '127.0.0.1'
PORT = 8008
BUFER_SIZE = 20


# Create server
server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


Resultado =""

class MyFuncs:
        def getTime(self):
            return time.strftime("%H:%M:%S")

server.register_instance(MyFuncs())

t = threading.Thread(target=server.serve_forever)

##########################cliente #############################################
portlist = [8005,8006,8007,8008,8009]
Hora =[]
Hpromedio = 0
t.start()
n=0
while True :
    while n<5:
        time.sleep(3)
        try:
        	s = xmlrpclib.ServerProxy("http://127.0.0.1:"+str(portlist[n]))	
        	Operar = s.getTime()
        	Hora.append(UTCtoSeconds(Operar))        	
       	except: 
       		pass

        n = n+1
    promedio = CPromedio(Hora)
    Hpromedio = SecondstoUTC(promedio)
    print Hpromedio
    n = 0
    Hora = []
sys.exit()


# Run the server's main loop
