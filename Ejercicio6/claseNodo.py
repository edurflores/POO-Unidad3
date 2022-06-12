class Nodo:
    __aparato = None
    __siguiente = None

    __posicion = 0 ### posicion del nodo en la lista

    def __init__(self,unaparato,xnum):
        self.__aparato = unaparato
        self.__siguiente = None
        self.__posicion = xnum

    def setSiguiente(self,sig):
        self.__siguiente = sig

    def getSiguiente(self):
        return self.__siguiente

    def getPosicion(self):
        return self.__posicion

    def getDato(self):
        return self.__aparato

    def incrementaPosicion(self):
        self.__posicion += 1