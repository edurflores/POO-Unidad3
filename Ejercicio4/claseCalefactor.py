class Calefactor:
    __marca = ''
    __modelo = ''

    def __init__(self,marc,mod):
        self.__marca = marc
        self.__modelo = mod

    def getModelo(self):
        return self.__modelo

    def getMarca(self):
        return self.__marca