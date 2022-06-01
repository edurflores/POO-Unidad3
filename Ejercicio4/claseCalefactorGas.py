from claseCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula = ''
    __calorias = 0 ### Kilocalorias/m3

    def __init__(self,marc,mod,matri,cal):
        super().__init__(marc,mod)
        self.__matricula = matri
        if type(cal) is int:
            self.__calorias = cal
        else:
            print('Error de parametro calorias en CalefactorGas.')

    def getCalorias(self):
        return self.__calorias