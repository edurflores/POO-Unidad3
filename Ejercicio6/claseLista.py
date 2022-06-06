from claseNodo import Nodo

class Lista:
    __comienzo = None

    __actual = None
    __indice = 0
    __tope = 0

    __numeronodo = 0 ### Numero que se adjuntara al nodo para indicar su posicion en la lista

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarAparato(self,unaparato):
        nodo = Nodo(unaparato,self.__numeronodo)
        self.__numeronodo += 1
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertaAparato(self,unAparato,xpos): ### Inserta un aparato en una posicion valida determinada
        if type(xpos) is int:
            if xpos < self.__numeronodo:
                nodo = Nodo(unAparato,xpos)
                nodo.setSiguiente(self.__comienzo)
                ###Ver lista de programacion procedural

    def listarDatosAparatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    ### Sigue funcion eliminar por x pero parece que no es tan necesaria