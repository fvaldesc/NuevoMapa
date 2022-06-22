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
parser.add_argument("-s", "--directorio_Programa_Mapa",  help="directorio Programa Mapa")
parser.add_argument("-c", "--directorio_Programa_Maquina",  help="directorioProgramaMaquina")

archivoBase="datos001-48-51-C5-4E-8E-2D"
numeroMAK  ="00-09-0F-AA-00-01"
archivoMapaMaquina="fer"
directorio_Programa_Mapa="D:\\Program Files (x86)\\Sistemed\\MAPA\\bin\\"
directorio_Programa_Maquina="D:\\Program Files (x86)\\ABPM\\data\\rosita\\SingleUser\\"

 
args = parser.parse_args()
if args.file:
        archivoBase= args.file
if args.mac:
        numeroMAK= args.mac
if args.mapa:
        archivoMapaMaquina= args.mapa
if args.directorio_Programa_Mapa:
        directorio_Programa_Mapa= args.directorio_Programa_Mapa
if args.directorio_Programa_Maquina:
        directorio_Programa_Maquina= args.directorio_Programa_Maquina
 

print (numeroMAK)
print(archivoMapaMaquina)
print(directorio_Programa_Mapa)
print(directorio_Programa_Maquina)

mapa=c.Mapa(numeroMAK,directorio_Programa_Mapa,directorio_Programa_Maquina)
mapa.leeDatosDeLaMaquina(archivoMapaMaquina)
mapa.ColocarDatosSegunFormatoMAPA()
mapa.CrearInformacionDelArchivo(archivoMapaMaquina) 
mapa.preparaArchivo(archivoMapaMaquina)

 