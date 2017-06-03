from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import threading
import os

IP = '127.0.0.1'
PUERTO = 9011
Maquinas = ['http://localhost:8001', 'http://localhost:8002']


def Escribir(nombre, cParcial, cTotal):
    for i in Maquinas:
        maquina = xmlrpclib.ServerProxy(i)
        retorno = maquina.Bloqueo(nombre)
    print "\n La pagina tiene ", cTotal, "lineas en total"
    print "Hay un maximo de ", cParcial, "lineas libres para escribir"
    print "solo se guardaran ", cTotal, "lineas si sobrepasa la capacidad"
    os.popen("notepad " + nombre)
    archivo = open(nombre, "r")
    contenido = archivo.read()
    lineas = len(open(nombre).readlines())
    if lineas > cTotal:
        print "\n Supero la capacidad maxima de almacenamiento, no se guardo todo el contenido"
        archivo = open(nombre, "r")
        contenido = archivo.read()
        archivo.close()
        contenido = contenido.split('\n')
        i = 0
        while i != cTotal:
            if i == 0:
                nuevo_contenido = contenido[0]
            else:
                nuevo_contenido += '\n' + contenido[i]
            i += 1
        archivo = open(nombre, "w")
        archivo.write(nuevo_contenido)
        archivo.close()
        contenido = nuevo_contenido
    for i in Maquinas:
        maquina = xmlrpclib.ServerProxy(i)
        retorno = maquina.Desbloqueo(nombre)
        if i != 'http://localhost:8001':
            retorno = maquina.ActualizarPagina(nombre, contenido)
            print "\n Pagina consistente"


#------------------------- CLIENTE--------------------------------#

while True:
    print "\n Proceso de la maquina 1"
    print "\n 1. Leer \n 2. Modificar \n 3. Listar memoria \n 4. Cerrar"
    opciones = ['1', '2', '3', '4']
    opcion = raw_input("Elija una opcion: ")

    if opcion == '1':
        nombre = raw_input("Ingrese el nombre de la pagina ")
        maquina = xmlrpclib.ServerProxy('http://localhost:8001')
        busqueda = maquina.BuscarPagina(nombre)
        if busqueda != -1:
            Archivo = open(nombre, "r")
            contenido = Archivo.read()
            Archivo.close()
            print contenido
        else:
            for i in Maquinas:
                if i != 'http://localhost:8001':
                    maquina = xmlrpclib.ServerProxy(i)
                    Copia = maquina.PedirCopia(nombre)
                    if Copia != -1:
                        if Copia != "No":
                            miMaquina = xmlrpclib.ServerProxy(
                                'http://localhost:8001')
                            retorno = miMaquina.AgregarCopia(
                                nombre, Copia[1], Copia[2])
                            Archivo = open(nombre, "w")
                            Archivo.write(Copia[0])
                            Archivo.close()
                            Archivo = open(nombre, "r")
                            contenido = Archivo.read()
                            Archivo.close()
                            print contenido
                        else:
                            print "\n No es posible acceder a la memoria en este momento, intente mas tarde"
                    else:
                        print "\n No existe la pagina referenciada"
    if opcion == '2':
        nombre = raw_input("Ingrese el nombre de la pagina ")
        maquina = xmlrpclib.ServerProxy('http://localhost:8001')
        busqueda = maquina.BuscarPagina(nombre)

        if busqueda == -1:
            for i in Maquinas:
                if i != 'http://localhost:8001':
                    maquina = xmlrpclib.ServerProxy(i)
                    Copia = maquina.PedirCopia(nombre)
                    if Copia != -1:
                        if Copia != "No":
                            miMaquina = xmlrpclib.ServerProxy(
                                'http://localhost:8001')
                            retorno = miMaquina.AgregarCopia(
                                nombre, Copia[1], Copia[2])
                            Archivo = open(nombre, "w")
                            Archivo.write(Copia[0])
                            Archivo.close()
                            Escribir(nombre, Copia[1], Copia[2])
                        else:
                            print "\n No es posible acceder a la memoria en este momento, intente mas tarde"
                    else:
                        print "\n No existe la pagina referenciada"
        else:
            if busqueda[2] == 0:
                Escribir(nombre, busqueda[0], busqueda[1])
            else:
                print "\n No es posible acceder a la memoria en este momento, intente mas tarde"
    if opcion == '3':
        print "\n"
        print "M1P1.txt"
        print "M2P1.txt"
