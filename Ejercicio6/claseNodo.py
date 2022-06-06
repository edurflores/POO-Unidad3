class Nodo:
    __aparato = None
    __siguiente = None

    __num = 0

    def __init__(self,unaparato,xnum):
        self.__aparato = unaparato
        self.__siguiente = None
        self.__num = xnum

    def setSiguiente(self,sig):
        self.__siguiente = sig

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__aparato