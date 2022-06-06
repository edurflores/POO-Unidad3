from claseAparato import Aparato

class Heladera(Aparato):
    __capacidad = 0 ### En litros
    __freezer = '' ### booleano
    __ciclica = '' ### booleano

    def __init__(self,marc,mod,col,pais,precio,cap,frez,cic):
        super().__init__(marc,mod,col,pais,precio)
        if type(cap) is int:
            self.__capacidad = cap
        else:
            print('Error de parametro capacidad en Heladera. Debe ser int.')
        if type(frez) is bool:
            self.__freezer = frez
        else:
            print('Error de parametro freezer en Heladera. Debe ser bool.')
        if type(cic) is bool:
            self.__ciclica = cic
        else:
            print('Error de parametro ciclica en Heladera. Debe ser bool.')

    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica