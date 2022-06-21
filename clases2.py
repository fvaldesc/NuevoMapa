class PatientData:
    def __init__(self):
        self.aBPMCount=""
        self.name=""
        self.id=""
        self.yearBegin=""
        self.monBegin=""
        self.dayBegin=""
        self.hourBegin=""
        self.minBegin=""
        self.secBegin=""
        self.maxPressValue=""
        self.awakeWarnOnOff=""
        self.awakeSysMaxValue=""
        self.awakeSysMinValue=""
        self.awakeDiaMaxValue=""
        self.awakeDiaMinValue=""
        self.asleepWarnOnOff=""
        self.asleepSysMaxValue=""
        self.asleepSysMinValue=""
        self.asleepDiaMaxValue=""
        self.asleepDiaMinValue=""
        self.display=""
        self.startKey=""
        self.awakeHour=""
        self.awakeMin=""
        self.awakeDuration=""
        self.asleepHour=""
        self.asleepMin=""
        self.asleepDuration=""
        self.apecialHourStart=""
        self.specialMinStart=""
        self.specialDuration=""
        self.specialHourEnd=""
        self.specialMinEnd=""
        self.addr=""
        self.gender=""
        self.birthday=""
        self.race=""
        self.height=""
        self.weight=""
        self.age=""
        self.phone=""
        self.medications=""
        self.referringPhys=""
        self.interprettingPhys=""
        self.comments=""
        self.clinicalInterp=""
        self.outpatientNo=""
        self.admissionNo=""
        self.bedNo=""
        self.departmentNo=""
        self.email=""

    def  setABPMCount(self,_aBPMCount):
                self.aBPMCount=_aBPMCount
    def  setName(self,_name):
                self.name=_name
    def  setEnumDeviceType(self,_enumDeviceType):
                self.enumDeviceType=_enumDeviceType
    def  setId(self,_id):
                self.id=_id
    def  setYearBegin(self,_yearBegin):
                self.yearBegin=_yearBegin
    def  setMonBegin(self,_monBegin):
                self.monBegin=_monBegin

    def  setDayBegin(self,_dayBegin):
                self.dayBegin=_dayBegin
    def  setHourBegin(self,_hourBegin):
                self.hourBegin=_hourBegin
    def  setMinBegin(self,_minBegin):
                self.minBegin=_minBegin
    def  setSecBegin(self,_secBegin):
                self.secBegin=_secBegin
    def  setMaxPressValue(self,_maxPressValue):
                self.maxPressValue=_maxPressValue
    def  setAwakeWarnOnOff(self,_awakeWarnOnOff):
                self.awakeWarnOnOff=_awakeWarnOnOff
    def  setAwakeSysMaxValue(self,_awakeSysMaxValue):
                self.awakeSysMaxValue=_awakeSysMaxValue

    def  setAwakeSysMinValue(self,_awakeSysMinValue):
                self.awakeSysMinValue=_awakeSysMinValue
    def  setAwakeDiaMaxValue(self,_awakeDiaMaxValue):
                self.awakeDiaMaxValue=_awakeDiaMaxValue
    def  setAwakeDiaMinValue(self,_awakeDiaMinValue):
                self.awakeDiaMinValue=_awakeDiaMinValue
    def  setAsleepWarnOnOff(self,_asleepWarnOnOff):
                self.asleepWarnOnOff=_asleepWarnOnOff
    def  setAsleepSysMaxValue(self,_asleepSysMaxValue):
                self.asleepSysMaxValue=_asleepSysMaxValue
    def  setAsleepSysMinValue(self,_asleepSysMinValue):
                self.asleepSysMinValue=_asleepSysMinValue
    def  setAsleepDiaMaxValue(self,_asleepDiaMaxValue):
                self.asleepDiaMaxValue=_asleepDiaMaxValue


    def  setAsleepDiaMinValue(self,_asleepDiaMinValue):
                self.asleepDiaMinValue=_asleepDiaMinValue
    def  setDisplay(self,_display):
                self.display=_display
    def  setStartKey(self,_startKey):
                self.startKey=_startKey
    def  setAwakeHour(self,_awakeHour):
                self.awakeHour=_awakeHour
    def  setAwakeMin(self,_awakeMin):
                self.awakeMin=_awakeMin
    def  setAwakeDuration(self,_awakeDuration):
                self.awakeDuration=_awakeDuration
    def  setAsleepHour(self,_asleepHour):
                self.asleepHour=_asleepHour

    def  setAsleepMin(self,_asleepMin):
                self.asleepMin=_asleepMin
    def  setAsleepDuration(self,_asleepDuration):
                self.asleepDuration=_asleepDuration
    def  setSpecialHourStart(self,_specialHourStart):
                self.specialHourStart=_specialHourStart
    def  setSpecialMinStart(self,_specialMinStart):
                self.specialMinStart=_specialMinStart
    def  setSpecialDuration(self,_specialDuration):
                self.specialDuration=_specialDuration
    def  setSpecialHourEnd(self,_specialHourEnd):
                self.specialHourEnd=_specialHourEnd
    def  setSpecialMinEnd(self,_specialMinEnd):
                self.specialMinEnd=_specialMinEnd
    def  setAddr(self,_addr):
                self.addr=_addr
    def  setGender(self,_gender):
                self.gender=_gender

    def  setBirthday(self,_birthday):
                self.gender=_birthday
    def  setRace(self,_race):
                self.gender=_race
    def  setHeight(self,_height):
                self.gender=_height
    def  setWeight(self,_weight):
                self.gender=_weight
    def  setAge(self,_age):
                self.gender=_age
    def  setPhone(self,_phone):
                self.gender=_phone
    def  setMedications(self,_medications):
                self.gender=_medications
    def  setReferringPhys(self,_referringPhys):
                self.gender=_referringPhys
    def  setInterprettingPhys(self,_interprettingPhys):
                self.interprettingPhys=_interprettingPhys
    def  setComments(self,_comments):
                self.comments=_comments
    def  setClinicalInterp(self,_clinicalInterp):
                self.clinicalInterp=_clinicalInterp
    def  setOutpatientNo(self,_outpatientNo):
                self.outpatientNo=_outpatientNo
    def  setAdmissionNo(self,_admissionNo):
                self.admissionNo=_admissionNo
    def  setBedNo(self,_bedNo):
                self.bedNo=_bedNo
    def  setDepartmentNo(self,_departmentNo):
                self.departmentNo=_departmentNo
    def  setEmail(self,_email):
                self.email=_email


    def print(self):
            print (self.patientData.aBPMCount)
            print (self.patientData.name)
            print (self.patientData.id)
            print (self.patientData.yearBegin)
            print (self.patientData.monBegin)
            print (self.patientData.dayBegin)
            print (self.patientData.hourBegin)
            print (self.patientData.minBegin)

            print (self.patientData.secBegin)
            print (self.patientData.maxPressValue)
            print (self.patientData.awakeWarnOnOff)
            print (self.patientData.awakeSysMaxValue)
            print (self.patientData.awakeSysMinValue)

            print (self.patientData.awakeDiaMaxValue)
            print (self.patientData.awakeDiaMinValue)
            print (self.patientData.asleepWarnOnOff)
            print (self.patientData.asleepSysMaxValue)
            print (self.patientData.asleepSysMinValue)

            print (self.patientData.asleepDiaMaxValue)
            print (self.patientData.asleepDiaMinValue)
            print (self.patientData.startKey)
            print (self.patientData.awakeHour)
            print (self.patientData.awakeMin)
            print (self.patientData.awakeDuration)
            print (self.patientData.asleepHour)
            print (self.patientData.asleepMin)
            print (self.patientData.asleepDuration)
            print (self.patientData.specialHourStart)
            print (self.patientData.specialMinStart)
            print (self.patientData.specialDuration)
            print (self.patientData.specialHourEnd)
            print (self.patientData.specialMinEnd)
            print (self.patientData.addr)
            print (self.patientData.gender)
            print (self.patientData.birthday)
            print (self.patientData.race)
            print (self.patientData.height)
            print (self.patientData.weight)
            print (self.patientData.age)
            print (self.patientData.phone)
            print (self.patientData.medications)
            print (self.patientData.referringPhys)
            print (self.patientData.interprettingPhys)
            print (self.patientData.comments)
            print (self.patientData.clinicalInterp)
            print (self.patientData.outpatientNo)
            print (self.patientData.admissionNo)
            print (self.patientData.bedNo)
            print (self.patientData.departmentNo)
            print (self.patientData.email)
 

class ExtraInfo:
    def __init__(self):
                print('Nombre ExtraInfo:') 
                self.enumDeviceType=1
                self.enumRemote=1
                self.enumDevKey=1
                self.enumProtocol=1
                self.strDeviceType=1
                self.dataMode=1
                self.protocolVersion_Main=1
                self.protocolVersion_Sub=1
                self.deviceVersion_Main=1
                self.deviceVersion_Sub=1
                self.fileVersion_Main=1
                self.fileVersion_Sub=1
                self.softWareVersion_Main=1
                self.softWareVersion_Sub=1
            
    def setEnumDeviceType(self,_enumDeviceType):
                self.enumDeviceType=_enumDeviceType
    def setEnumRemote(self,_enumRemote):
                self.enumRemote=_enumRemote
    def setEnumDevKey(self,_enumDevKey):
                self.enumDevKey=_enumDevKey
    def setEnumProtocol(self,_enumProtocol):
                self.enumProtocol=_enumProtocol
    def setStrDeviceType(self,_strDeviceType):
                self.strDeviceType=_strDeviceType
    def setDataMode(self,_dataMode):
                self.dataMode=_dataMode
    def setProtocolVersion_Main(self,_protocolVersion_Main):
                self.protocolVersion_Main=_protocolVersion_Main
    def setProtocolVersion_Sub(self,_protocolVersion_Sub):
                self.protocolVersion_Sub=_protocolVersion_Sub
    def setDeviceVersion_Main(self,_deviceVersion_Main):
                self.deviceVersion_Main=_deviceVersion_Main
    def setDeviceVersion_Sub(self,_deviceVersion_Sub):
                self.deviceVersion_Sub=_deviceVersion_Sub
    def setFileVersion_Main(self,_fileVersion_Main):
                self.fileVersion_Main=_fileVersion_Main
    def setFileVersion_Sub(self,_fileVersion_Sub):
                self.fileVersion_Sub=_fileVersion_Sub
    def setSoftWareVersion_Main(self,_softWareVersion_Main):
                self.softWareVersion_Main=_softWareVersion_Main
    def setSoftWareVersion_Sub(self,_softWareVersion_Sub):
                self.softWareVersion_Sub=_softWareVersion_Sub

    def print(self):
            print (self.enumDeviceType)
            print (self.enumRemote)
            print (self.enumDevKey)
            print (self.enumProtocol)
            print (self.strDeviceType)
            print (self.dataMode)
            print (self.protocolVersion_Main)
            print (self.protocolVersion_Sub)
            print (self.deviceVersion_Main)
            print (self.deviceVersion_Sub)
            print (self.fileVersion_Main)
            print (self.fileVersion_Sub)
            print (self.softWareVersion_Main)
            print (self.softWareVersion_Sub)


class Abpm:
    def __init__(self):
                print('Nombre Abpm:') 
                self.yearBegin=1
                self.monBegin=1
                self.dayBegin=1
                self.hourBegin=1
                self.minBegin=1
                self:secBegin=1
    def setYearBegin(self,_yearBegin):
        self.yearBegin=_yearBegin
    def setMonBegin(self,_monBegin):
        self.monBegin=_monBegin
    def setDayBegin(self,_dayBegin):
        self.dayBegin=_dayBegin
    def setHourBegin(self,_hourBegin):
        self.hourBegin=_hourBegin
    def setMinBegin(self,_minBegin):
        self._minBegin=_minBegin
    def setSecBegin(self,_secBegin):
        self.secBegin=_secBegin

class Maquina:
    def __init__(self):
        print('Nombre Maquina:') 
        self.patientData = PatientData()
        self.extraInfo   = ExtraInfo()
        self.abpmdata    = Abpm()
        self.datosLeidoDeLaMaquina=[]
    
    def agregarDatosDeLaMaquina(self,s):
            if s[1:2]== "=":
                self.datosLeidoDeLaMaquina.append(s)
    
    def printDatosLeidosDeLaMaquina(self):
        i = 1
        s=self.datosLeidoDeLaMaquina[0]
        systole     = str(int(s[18:20],16)) 
        diastole    = str(int(s[22:24],16))
        fr          = str(int(s[30:32],16))
        pam         = str(int(s[26:28],16))
        hora        = str(int(s[10:12],16))+":"+str(int(s[12:14],16))
        a="2022/02/05 " + hora + "," + systole + "," + diastole + "," + fr + "," + pam + "," + "0" + "," + '"'+ "comemntario" + '"##'
        s="[data]"+'\n'+"valor1="+a
        while i < len(self.datosLeidoDeLaMaquina):
            ss=self.datosLeidoDeLaMaquina[i]
            systole     = str(int(ss[18:20],16)) 
            diastole    = str(int(ss[22:24],16))
            fr          = str(int(ss[30:32],16))
            pam         = str(int(ss[26:28],16))
            hora        = str(int(ss[10:12],16))+":"+str(int(ss[12:14],16))
            a="2022/02/05 " + hora + "," + systole + "," + diastole + "," + fr + "," + pam + "," + "0" + "," + '"'+ "comemntario" + '"##'
            s=s+a
            i += 1
        
        return s



    def agregarAbpmdata(self,s):
            if s.find("YearBegin") != -1:
                self.abpmdata.setYearBegin(s)
            if s.find("MonBegin") != -1:
                self.abpmdata.setMonBegin(s)
            if s.find("DayBegin") != -1:
                self.abpmdata.setDayBegin(s)
            if s.find("HourBegin") != -1:
                self.abpmdata.setHourBegin(s)
            if s.find("MinBegin") != -1:
                self.abpmdata.setMinBegin(s)
            if s.find("SecBegin") != -1:
                self.abpmdata.setSecBegin(s)
    def agregarPatientData(self,s):
            if s.find("ABPMCount") != -1:
                self.patientData.setABPMCount(s)
            if s.find("Name") != -1:
                self.patientData.setName(s)
            if s.find("ID") != -1:
                self.patientData.setId(s)
            if s.find("YearBegin") != -1:
                self.patientData.setYearBegin(s)
            if s.find("DayBegin") != -1:
                self.patientData.setDayBegin(s)
            if s.find("HourBegin") != -1:
                self.patientData.setHourBegin(s)
            if s.find("MinBegin") != -1:
                self.patientData.setMinBegin(s)
            if s.find("SecBegin") != -1:
                self.patientData.setSecBegin(s)
 
            if s.find("MaxPressValue") != -1:
                self.patientData.setMaxPressValue(s)
            if s.find("AwakeWarnOnOff") != -1:
                self.patientData.setAwakeWarnOnOff(s)
            if s.find("AwakeSysMaxValue") != -1:
                self.patientData.setAwakeSysMaxValue(s)
            if s.find("AwakeSysMinValue") != -1:
                self.patientData.setAwakeSysMinValue(s)
            if s.find("AwakeDiaMaxValue") != -1:
                self.patientData.setAwakeDiaMaxValue(s)
            if s.find("AwakeDiaMinValue") != -1:
                self.patientData.setAwakeDiaMinValue(s)
            if s.find("AsleepWarnOnOff") != -1:
                self.patientData.setAsleepWarnOnOff(s)
            if s.find("AsleepSysMaxValue") != -1:
                self.patientData.setAsleepSysMaxValue(s)
 
            if s.find("AsleepSysMinValue") != -1:
                self.patientData.setAsleepSysMinValue(s)
            if s.find("AsleepDiaMaxValue") != -1:
                self.patientData.setAsleepDiaMaxValue(s)
            if s.find("AsleepDiaMinValue") != -1:
                self.patientData.setAsleepDiaMinValue(s)
            if s.find("Display") != -1:
                self.patientData.setDisplay(s)
            if s.find("StartKey") != -1:
                self.patientData.setStartKey(s)
            if s.find("AwakeHour") != -1:
                self.patientData.setAwakeHour(s)
            if s.find("AwakeMin") != -1:
                self.patientData.setAwakeMin(s)
            if s.find("AwakeDuration") != -1:
                self.patientData.setAwakeDuration(s)
            if s.find("AsleepHour") != -1:
                self.patientData.setAsleepHour(s)
            if s.find("AsleepMin") != -1:
                self.patientData.setAsleepMin(s)
            if s.find("AsleepDuration") != -1:
                self.patientData.setAsleepDuration(s)
            if s.find("SpecialHourStart") != -1:
                self.patientData.setSpecialHourStart(s)
            if s.find("SpecialDuration") != -1:
                self.patientData.setSpecialDuration(s)
            if s.find("SpecialDuration") != -1:
                self.patientData.setSpecialDuration(s)
            if s.find("SpecialHourEnd") != -1:
                self.patientData.setSpecialHourEnd(s)
            if s.find("SpecialMinEnd") != -1:
                self.patientData.setSpecialMinEnd(s)
            if s.find("Addr") != -1:
                self.patientData.setAddr(s)
            if s.find("Gender") != -1:
                self.patientData.setGender(s)
            if s.find("Birthday") != -1:
                self.patientData.setBirthday(s)
            if s.find("Race") != -1:
                self.patientData.setRace(s)
            if s.find("Height") != -1:
                self.patientData.setHeight(s)
            if s.find("Weight") != -1:
                self.patientData.setWeight(s)
            if s.find("Age") != -1:
                self.patientData.setAge(s)
            if s.find("Phone") != -1:
                self.patientData.setPhone(s)
            if s.find("Medications") != -1:
                self.patientData.setMedications(s)
            if s.find("ReferringPhys") != -1:
                self.patientData.setReferringPhys(s)
            if s.find("InterprettingPhys") != -1:
                self.patientData.setInterprettingPhys(s)
            if s.find("Comments") != -1:
                self.patientData.setComments(s)
            if s.find("ClinicalInterp") != -1:
                self.patientData.setClinicalInterp(s)
 
            if s.find("OutpatientNo") != -1:
                self.patientData.setOutpatientNo(s)
            if s.find("AdmissionNo") != -1:
                self.patientData.setAdmissionNo(s)
            if s.find("BedNo") != -1:
                self.patientData.setBedNo(s)
            if s.find("DepartmentNo") != -1:
                self.patientData.setDepartmentNo(s)
            if s.find("Email") != -1:
                self.patientData.setEmail(s)
    def agregarExtraInfo(self,s):
            if s.find("enumDeviceType") != -1:
                self.extraInfo.setEnumDeviceType(s)
            if s.find("enumRemote") != -1:
                self.extraInfo.setEnumRemote(s)
            if s.find("enumDevKey") != -1:
                self.extraInfo.setEnumDevKey(s)
            if s.find("enumProtocol") != -1:
                self.extraInfo.setEnumProtocol(s)
            if s.find("strDeviceType") != -1:
                self.extraInfo.setStrDeviceType(s)
            if s.find("DataMode") != -1:
                self.extraInfo.setDataMode(s)
            if s.find("ProtocolVersion_Main") != -1:
                self.extraInfo.setProtocolVersion_Main(s)
            if s.find("ProtocolVersion_Sub") != -1:
                self.extraInfo.setProtocolVersion_Sub(s)
            if s.find("DeviceVersion_Main") != -1:
                self.extraInfo.setDeviceVersion_Main(s)
            if s.find("DeviceVersion_Sub") != -1:
                self.extraInfo.setDeviceVersion_Sub(s)
            if s.find("FileVersion_Main") != -1:
                self.extraInfo.setFileVersion_Main(s)
            if s.find("strDeviFileVersion_SubceType") != -1:
                self.extraInfo.setStrDeviFileVersion_SubceType(s)
            if s.find("SoftWareVersion_Main") != -1:
                self.extraInfo.setSoftWareVersion_Main(s)
            if s.find("SoftWareVersion_Sub") != -1:
                self.extraInfo.setSoftWareVersion_Sub(s)