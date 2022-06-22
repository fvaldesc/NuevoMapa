class Clinicos:
    def __init__(self):
 #        print('Nombre Clinicos:') 
         self.s =""
    def print (self):
            s="[Clinicos]"+'\n'
            s=s+"Antecedentes=."+'\n'
            s=s+"Sintomas=."+'\n'
            return s
class Medicotratante:
    def __init__(self):
 #       print('Nombre Medicotratante:') 
         self.s =""
    def print (self):
            s="[Medico tratante]"+'\n'
            s=s+"NombreMedico=."+'\n'
            return s
class Medicaciones:
    def __init__(self):
 #        print('Nombre Medicaciones:') 
         self.s =""
    def print (self):
            s="[Medicaciones]"+'\n'
            s=s+"Medicaciones=."+'\n'
            return s
class Sueno:
    def __init__(self):
 #       print('Nombre Sueno:') 
         self.s =""
    def print (self):
            s="[Sueno]"+'\n'
            s=s+"SeAcosto=."+'\n'
            s=s+"SeDurmio=."+'\n'
            s=s+"SeDesperto=."+'\n'
            s=s+"SeLevanto=."+'\n'
            s=s+"ComoDurmio=."+'\n'
            return s
class Comidas:
    def __init__(self):
 #       print('Nombre Comidas:') 
         self.s =""
    def print (self):
            s="[Comidas]"+'\n'
            s=s+"Desayuno=."+'\n'
            s=s+"Almuerzo=."+'\n'
            s=s+"Once=."+'\n'
            s=s+"Cena=."+'\n'
            return s
class Trabajo:
    def __init__(self):
 #        print('Nombre Trabajo:') 
         self.s =""
    def print (self):
            s="[Trabajo]"+'\n'
            s=s+"TrabajoInicio=."+'\n'
            s=s+"TrabajoFin=."+'\n'
            return s
class Observaciones:
    def __init__(self):
 #       print('Nombre Observaciones:') 
         self.s =""
    def print (self):
            s="[Observaciones]"+'\n'
            s=s+"Observaciones=."+'\n'
            return s
class DatosDeLaMaquina:
    def __init__(self):
 #               print('Nombre DatosDeLaMaquina:') 
                self.datos=[]
    def print (self):
            s="[Observaciones]"+'\n'
            s=s+"Observaciones=."+'\n'
            return s
class Persona:
    def __init__(self,_mac):
 #               print('Nombre Persona:') 
                self.tipo="."
                self.id="."
                self.tipoId="."
                self.nombres="."
                self.apellidos="."
                self.altura="."
                self.peso="."
                self.cintura="."
                self.rut="."
                self.kernel="."
                self.cliente="."
                self.telefono="."
                self.fax="."
                self.mail="."
                self.fechaNacimiento="."
                self.sexo="."
                self.mac=_mac
                
 
    def setTipo(self,_tipo):
                self.tipo=_tipo    
    def setRut(self,_rut):
                self.rut=_rut
    def setId(self,_id):
                self.id=_id
    def setNombre(self,_nombre):
                self.nombres=_nombre
    def setApellido(self,_apellido):
                self.apellidos=_apellido
    def setAltura(self,_altura):
                self.altura=_altura
    def setMac(self,_mac):
                self.mac=_mac
    def print (self):
            s= "Tipo=2"+'\n'
            s=s+"[Personales]"+'\n'
            s=s+"ID="+self.id+'\n'
            s=s+"TipoID="+self.tipoId+'\n'
            s=s+"Nombres="+self.nombres+'\n'
            s=s+"Apellidos="+self.apellidos+'\n'
            s=s+"Altura="+self.altura+'\n'
            s=s+"Peso="+self.peso+'\n'
            s=s+"Cintura="+self.cintura+'\n'
            s=s+"Rut="+self.rut+'\n'
            s=s+"Kernel="+self.kernel+'\n'
            s=s+"Cliente="+self.cliente+'\n'
            s=s+"Telefono="+self.telefono+'\n'
            s=s+"Fax="+self.fax+'\n'
            s=s+"Mail="+self.mail+'\n'
            s=s+"FechaNacimiento="+self.fechaNacimiento+'\n'
            s=s+"Sexo="+self.sexo+'\n'
            s=s+"MAC="+self.mac+'\n'
            return s