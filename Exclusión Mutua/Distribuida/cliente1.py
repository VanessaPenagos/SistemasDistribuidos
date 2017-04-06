from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from datetime import datetime
import xmlrpclib
import threading
import time
import sys
import random

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


class MyFuncs:
    def __init__(self):
        self.MisRecursos = ['3','4']
        self.EnEspera = []
        self.Ocupado = ['4']
    def Precurso(self,msn):
        rec, proceso, tiempo = msn.split()
        if rec in self.MisRecursos:
            if rec not in self.Ocupado:
                okmsg = ('OK',proceso)
                return okmsg
        self.EnEspera.append(proceso)
        return "Espera"

    def SacarRecurso(self,recurso):
        i= self.MisRecursos.index(recurso)
        self.MisRecursos.pop(i)
        return recurso

    def DevolverRecurso(self,recurso):
        self.MisRecursos.append(recurso)
        return recurso

server.register_instance(MyFuncs())


t = threading.Thread(target=server.serve_forever)

##########################cliente #############################################
portlist = [8005,8006,8007]
t.start()
n=0
while True :
    while n<3:
        time.sleep(2)
        try:
            s = xmlrpclib.ServerProxy("http://127.0.0.1:"+str(portlist[n]))    
            solicitud = s.Precurso('3 '+str(n)+" "+ time.strftime("%H:%M:%S"))
            if solicitud != 'Espera':
                if solicitud[0] == 'OK':
                    ProcesoOk= solicitud[1]
            print "Espera" 
        except: 
            print "Fallo en", portlist[n]
            pass
        n=n+1
    s1 = xmlrpclib.ServerProxy("http://127.0.0.1:"+str(portlist[int(ProcesoOk)]))
    tomo = s1.SacarRecurso('3')
    print "Se toma", tomo
    time.sleep(random.randint(2,3))
    dejo = s1.DevolverRecurso('3')
    print "Se deja", dejo
    n=0

sys.exit()
