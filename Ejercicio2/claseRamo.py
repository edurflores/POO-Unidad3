class Ramo:
    __tamanio = '' ### chico, mediano o grande
    __flores = []

    def __init__(self,tam,flor=None):
        self.__tamanio = tam

    def setTamanio(self,tam):
        self.__tamanio = tam

    def agregarFlor(self,flor,cantidad):
        if type(cantidad) is int:
            for i in range(cantidad):
                self.__flores.append(flor)
            print('Se ha agregado {} flor/es al ramo.'.format(cantidad))
        else:
            print('Error de parametro cantidad.')

    def getFlores(self):
        return self.__flores

    def getTamanio(self):
        return self.__tamanio