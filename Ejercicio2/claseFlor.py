class Flor:
    __numero = 0
    __nombre = ''
    __color = ''
    __descripcion = ''

    def __init__(self,num,nom,col=''):
        if type(num) is int:
            self.__numero = num
        else:
            print('Error de parametro numero en flor.')
        self.__nombre = nom
        self.__color = col
        self.__descripcion = self.__nombre + ' ' + self.__color

    def setColor(self,col):
        self.__color = col

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    def __str__(self):
        return 'Numero: ' + str(self.__numero) + ' | Nombre: ' + self.__nombre