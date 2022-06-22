import clases2 as d
import clases3 as e
import pprint
import os
import numpy as np
from zipfile import ZipFile
from secrets import token_bytes
import argparse
import shutil 

 

class Comprimir:
    def __init__(self,_directorioProgramaMapa):
   #     print('Nombre Comprimir:') 
        self.nombre = ""
        self.directorioProgramaMapa=_directorioProgramaMapa

    def ejecutar(self,_nombre):
        self.nombre=_nombre
        self.__comprimeZIP()
        self.__crearArchivoZIPConXOR()
        salida=self.directorioProgramaMapa+'\\'+"pendientes"+'\\'+_nombre+"XOR.tmp"
 
        shutil.copy(".\\temp\\"+_nombre+"XOR.tmp", salida)

    def __comprimeZIP(self):
        filenames = [self.nombre+".sal"]
        with ZipFile(".\\temp\\"+self.nombre+".zip", mode="w") as archive:
            for filename in filenames:
                archive.write(".\\temp\\"+filename)
        
    def __crearArchivoZIPConXOR(self):
 
        file = open(".\\temp\\"+self.nombre+".zip", "rb")
        fileSalida = open(".\\temp\\"+self.nombre+"XOR.tmp", "wb")
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
     #   print('Nombre Archivo:') 
        self.persona        =e.Persona(_mac)
        self.clinicos       =e.Clinicos()
        self.medicotratante =e.Medicotratante()
        self.medicaciones   =e.Medicaciones()
        self.sueno          =e.Sueno()
        self.trabajo        =e.Trabajo()
        self.observaciones  =e.Observaciones()
        self.comidas        =e.Comidas()
        self.datos          =""

class Mapa:
    def __init__(self,_mac,_directorioProgramaMapa,_directorioProgramaMaquina):
        self.archivo = Archivo(_mac)
        self.maquina = d.Maquina()
        self.mac=_mac
        self.comprimir = Comprimir(_directorioProgramaMapa)
        self.directorioProgramaMapa=_directorioProgramaMapa
        self.directorioProgramaMaquina=_directorioProgramaMaquina

    def preparaArchivo(self,_nombre):
        self.comprimir.ejecutar(_nombre)

    def ColocarDatosSegunFormatoMAPA(self):
 

        self.archivo.persona.nombre =  self.maquina.patientData.name
        self.archivo.persona.rut    =  self.maquina.patientData.id
        self.archivo.persona.altura =  self.maquina.patientData.height        
        self.archivo.persona.peso   =  self.maquina.patientData.weight       
        self.archivo.persona.altura =  self.maquina.patientData.age 
        self.archivo.persona.mac    =  self.mac
        self.archivo.datos          =  self.maquina.printDatosLeidosDeLaMaquina()   

    def CrearInformacionDelArchivo(self,archivo):
  
        archivoTexto=open(".\\temp\\"+archivo+".sal","w") 
        archivoTexto.write(self.archivo.persona.print())
        archivoTexto.write(self.archivo.clinicos.print())
        archivoTexto.write(self.archivo.medicotratante.print())
        archivoTexto.write(self.archivo.medicaciones.print())
        archivoTexto.write(self.archivo.sueno.print())
        archivoTexto.write(self.archivo.comidas.print())
        archivoTexto.write(self.archivo.trabajo.print())
        archivoTexto.write(self.archivo.observaciones.print())
        archivoTexto.write(self.archivo.datos)
         
 
        archivoTexto.close()
    def leeDatosDeLaMaquina(self,nombre):
        fichero = open(self.directorioProgramaMaquina+'\\'+nombre+'.awp')
        lineasArchivos = []
 
        lineas = fichero.readlines()
        for linea in lineas:
            lineasArchivos.append(linea)
        for a in lineasArchivos:
            self.maquina.agregarExtraInfo(a)
            self.maquina.agregarPatientData(a)
            self.maquina.agregarAbpmdata(a)
            self.maquina.agregarDatosDeLaMaquina(a)
            self.maquina.agregarComentarioDeLaMaquina(a)
            
 