import abc
from abc import ABC
class Aparato:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisfabric = ''
    __preciobase = 0.0

    def __init__(self,marca,modelo,color,paisfabric,preciobase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisfabric = paisfabric
        if type(preciobase) is float:
            self.__preciobase = preciobase
        else:
            print('Error de parametro precio base en clase Aparato.')

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getPrecioBase(self):
        return self.__preciobase

    def getColor(self):
        return self.__color

    def getPaisFabric(self):
        return self.__paisfabric

    def __str__(self): ### Basado en el inciso 6
        cadena = 'Marca: {}.\n'.format(self.__marca)
        cadena += 'Pais de fabricacion: {}.\n'.format(self.__paisfabric)
        return cadena

    @abc.abstractmethod
    def toJSON(self): ### Metodo abstracto
        pass