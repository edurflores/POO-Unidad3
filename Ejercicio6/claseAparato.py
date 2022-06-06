class Aparato:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisfabric = ''
    __preciobase = 0.0

    def __init__(self,marc,mod,col,pais,precio):
        self.__marca = marc
        self.__modelo = mod
        self.__color = col
        self.__paisfabric = pais
        if type(precio) is float:
            self.__preciobase = precio
        else:
            print('Error de parametro precio base en clase Aparato.')

    def getMarca(self):
        return self.__marca

    def getPrecioBase(self):
        return self.__preciobase

    def __str__(self): ### Basado en el inciso 6
        cadena = 'Marca: {}.\n'.format(self.__marca)
        cadena += 'Pais de fabricacion: {}.\n'.format(self.__paisfabric)
        return cadena