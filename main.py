import pprint
import os
import numpy as np
from zipfile import ZipFile
from secrets import token_bytes
import argparse
 
import clases  as c





parser = argparse.ArgumentParser() 
parser.add_argument("-f", "--file", help="Nombre de archivo *.xml")
parser.add_argument("-m", "--mac",  help="Numero MAK")
parser.add_argument("-k", "--mapa",  help="Arcbivo mapa")

archivoBase="datos001-48-51-C5-4E-8E-2D"
numeroMAK  ="00-09-0F-AA-00-01"
archivoMapaMaquina="2022050220460501"
try:
    args = parser.parse_args()
    if args.file:
        archivoBase= args.file
    if args.mac:
        numeroMAK= args.mac
    if args.mapa:
        archivoMapaMaquina= args.mapa
except :
        print ("error")
print (numeroMAK)
print(archivoBase)

mapa=c.Mapa(numeroMAK)
mapa.leeDatosDeLaMaquina(archivoMapaMaquina)
mapa.ColocarDatosSegunFormatoMAPA()
mapa.CrearInformacionDelArchivo(archivoMapaMaquina) 
mapa.preparaArchivo(archivoMapaMaquina)
 