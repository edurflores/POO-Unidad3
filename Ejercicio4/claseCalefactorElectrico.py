from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potenciaMaxima = 0 ### En watts

    def __init__(self,marca,modelo,pot):
        super().__init__(marca,modelo)
        if type(pot) is int:
            self.__potenciaMaxima = pot
        else:
            print('Error de parametro potencia en CalefactorElectrico.')

    def getPotencia(self):
        return self.__potenciaMaxima