from claseAparato import Aparato

class Heladera(Aparato):
    __capacidad = 0 ### En litros
    __freezer = bool ### booleano
    __ciclica = bool ### booleano

    def __init__(self,marca,modelo,color,paisfabric,preciobase,capacidad,freezer,ciclica):
        super().__init__(marca,modelo,color,paisfabric,preciobase)
        if type(capacidad) is int:
            self.__capacidad = capacidad
        else:
            print('Error de parametro capacidad en Heladera. Debe ser int.')
        if type(freezer) is bool:
            self.__freezer = freezer
        else:
            print('Error de parametro freezer en Heladera. Debe ser bool.')
        if type(ciclica) is bool:
            self.__ciclica = ciclica
        else:
            print('Error de parametro ciclica en Heladera. Debe ser bool.')

    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getMarca(),
                modelo=self.getModelo(),
                color=self.getColor(),
                paisfabric=self.getPaisFabric(),
                preciobase=self.getPrecioBase(),
                capacidad=self.__capacidad,
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d