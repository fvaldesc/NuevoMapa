import clases2 as d
import clases3 as e
import pprint
import os
import numpy as np
from zipfile import ZipFile
from secrets import token_bytes
import argparse
 

 

class Comprimir:
    def __init__(self):
        print('Nombre Comprimir:') 
        self.nombre = ""

    def ejecutar(self,_nombre):
        self.nombre=_nombre
        self.__comprimeZIP()
        self.__crearArchivoZIPConXOR()

    def __comprimeZIP(self):
        filenames = [self.nombre+".sal"]
        print(self.nombre+".zip")
        with ZipFile(self.nombre+".zip", mode="w") as archive:
            for filename in filenames:
                archive.write(filename)
        
    def __crearArchivoZIPConXOR(self):
        file = open(self.nombre+".zip", "rb")
        fileSalida = open(self.nombre+"XOR.tmp", "wb")
        byte = file.read(1)
        key = bytes(token_bytes(1))
        fileSalida.write(key)
        while byte:
            encrypted_text = self.__crypt_xor(byte, key)
            fileSalida.write(encrypted_text)
   #         print(byte,encrypted_text)
            byte = file.read(1)
 
        fileSalida.close()
 
    def __crypt_xor(self,message, key):
        result = bytearray(message)
        for i, k in enumerate(self.__cycle(key, len(message))):
            result[i] ^= k
        return result

    def __cycle(self,s, max):
        n = len(s)
        return (s[i % n] for i in range(max))


class Archivo:
    def __init__(self,_mac):
        print('Nombre Archivo:') 
        self.persona        =e.Persona(_mac)
        self.clinicos       =e.Clinicos()
        self.medicotratante =e.Medicotratante()
        self.medicaciones   =e.Medicaciones()
        self.sueno          =e.Sueno()
        self.trabajo        =e.Trabajo()
        self.observaciones  =e.Observaciones()

class Mapa:
    def __init__(self,_mac):
        print('Nombre Mapa:') 
        self.archivo = Archivo(_mac)
        self.maquina = d.Maquina()
        self.mac=_mac
        self.comprimir = Comprimir()

    def preparaArchivo(self,_nombre):
        self.comprimir.ejecutar(_nombre)

    def ColocarDatosSegunFormatoMAPA(self):
        self.archivo.persona.nombre =  self.maquina.patientData.name
        self.archivo.persona.rut    =  self.maquina.patientData.id
        self.archivo.persona.mac    =  self.mac

    def CrearInformacionDelArchivo(self,archivo):
        archivoTexto=open(archivo+".sal","w") 
        archivoTexto.write(self.archivo.persona.print())
        archivoTexto.write(self.maquina.printDatosLeidosDeLaMaquina())
        archivoTexto.close()


    def leeDatosDeLaMaquina(self,nombre):
        fichero = open(nombre+'.awp')
        lineasArchivos = []
        lineas = fichero.readlines()
        for linea in lineas:
            lineasArchivos.append(linea)
        for a in lineasArchivos:
            self.maquina.agregarExtraInfo(a)
            self.maquina.agregarPatientData(a)
            self.maquina.agregarAbpmdata(a)
            self.maquina.agregarDatosDeLaMaquina(a)
 