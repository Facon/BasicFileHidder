# -*- coding: cp1252 -*-

import os
import sys

firma = "[-FIRMA-]"

def camuflar():
	nombre_archivo = sys.argv[2]
	imagen = "prueba.png"
	f = open(nombre_archivo, 'rb')
	contenido = f.read()
	d = open(imagen, 'rb')
	contenido_imagen = d.read()
	x = open("camuflado.png", 'wb')
	contenido = contenido_imagen + firma + contenido
	x.write(contenido)
	f.close()
	x.close()
def descubierto():
	nombre_archivo = sys.argv[2]
	f = open(nombre_archivo, 'rb')
	d = open("descubierto.zip", 'wb')
	contenido = f.read()
	contenido = contenido.split(firma)
	d.write(contenido[1])
	f.close()
	d.close()	
if sys.argv[1] == "-c" and sys.argv[2] != "":
	camuflar()
	print "¡Camuflado!"
elif sys.argv[1] == "-d" and sys.argv[2] != "":
	descubierto()
	print "¡Descubierto!"
elif sys.argv[1] == "-h":
	print "\n\t-c camuflar\n\t-d descubrir\nSintaxis: python camuflador.py -argumento nombre_archivo"
else:
	print "¡No ha escrito argumentos!, añada '-h' para ayuda."
