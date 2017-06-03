from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import threading
import os

IP = '127.0.0.1'
PUERTO = 9021
Maquinas = ['http://localhost:8001', 'http://localhost:8002']

def Escribir(nombre, cParcial, cTotal):
    print "La pagina tiene ", cTotal, "lineas en total"
    print "Hay un maximo de ", cParcial, "lineas libres para escribir"
    print "solo se guardaran ", cTotal, "lineas si sobrepasa la capacidad"
    os.popen("gedit"+ nombre)
    archivo = open(nombre,"r")
    contenido = archivo.read()
    lineas = len(open(nombre).readlines())
    if lineas > cTotal:
        print "Supero la capacidad maxima de almacenamiento, no se guardo todo el contenido"
#       **Se borran las demas lineas**
    for i in Maquinas:
        if i != 'http://localhost:8001':
            maquina = xmlrpclib.ServerProxy(i)
            retorno = maquina.ActualizarPagina(nombre, contenido)
            print "Pagina consistente"
#------------------------- CLIENTE--------------------------------#

while True:
    print "Proceso de la maquina 1"
    print "\n 1. Leer \n 2. Modificar \n 3. Listar memoria \n 4. Cerrar"
    opciones = ['1', '2', '3', '4']
    opcion = raw_input("Elija una opcion: ")

    if opcion == '1':
        nombre = raw_input("Ingrese el nombre de la pagina ")
        maquina = xmlrpclib.ServerProxy('http://localhost:8002')
        busqueda = maquina.BuscarPagina(nombre)
        if busqueda != -1:
            Archivo = open(nombre, "r")
            contenido = Archivo.read()
            Archivo.close()
            print contenido
        else:
            for i in Maquinas:
                if i != 'http://localhost:8002':
                    maquina = xmlrpclib.ServerProxy(i)
                    Copia = maquina.PedirCopia(nombre)
                    if Copia != -1 :
                        miMaquina = xmlrpclib.ServerProxy('http://localhost:8002')
                        retorno = miMaquina.AgregarCopia(nombre, Copia[1])
                        Archivo = open(nombre, "w")
                        Archivo.write(Copia[0])
                        Archivo.close()
                        Archivo = open(nombre, "r")
                        contenido = Archivo.read()
                        Archivo.close()
                        print contenido
                    else:
                        print "No existe la pagina referenciada"
    if opcion == '2':
        nombre = raw_input("Ingrese el nombre de la pagina ")
        maquina = xmlrpclib.ServerProxy('http://localhost:8002')
        busqueda = maquina.BuscarPagina(nombre)
        if busqueda == -1:
            for i in Maquinas:
                if i != 'http://localhost:8002':
                    maquina = xmlrpclib.ServerProxy(i)
                    Copia = maquina.PedirCopia(nombre)
                    if Copia != -1 :
                        miMaquina = xmlrpclib.ServerProxy('http://localhost:8002')
                        retorno = miMaquina.AgregarCopia(nombre, Copia[1])
                        Archivo = open(nombre, "w")
                        Archivo.write(Copia[0])
                        Archivo.close()
                        Escribir(nombre, Copia[1], Copia[2])
                    else:
                        print "No existe la pagina referenciada"
        if(busqueda != -1 and Copia != -1):
            Escribir(nombre, busqueda[0], busqueda[1])
