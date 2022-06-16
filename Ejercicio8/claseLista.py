from claseNodo import Nodo

class Lista:
    __comienzo = None

    __actual = None
    __indice = 0
    __tope = 0

    __numeronodo = 0 ### Numero de nodos de la lista.

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

    def agregarPersona(self,unapersona):
        nodo = Nodo(unapersona,self.__numeronodo)
        self.__numeronodo += 1
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertaPersona(self,unapersona,xpos): ### Inciso 1
        encontrado = False
        if type(xpos) is int:
            aux = self.__comienzo
            anterior = aux
            if xpos < self.__tope:
                while aux != None and encontrado == False:
                    if aux.getPosicion() == xpos:
                        nodo = Nodo(unapersona,xpos)
                        anterior.setSiguiente(nodo)
                        aux.incrementaPosicion()
                        nodo.setSiguiente(aux)
                        encontrado = True
                        self.__tope += 1
                        print('Nodo insertado.')
                    else:
                        anterior = aux
                        aux = aux.getSiguiente()
                while aux != None and aux.getPosicion() < self.__tope:
                    aux.incrementaPosicion()
                    aux = aux.getSiguiente()
            else:
                print('La posicion dada supera el tope de la lista. No pudo insertarse.')

    def buscaPosicion(self,xpos): ### Inciso 3, devuelve el dato en la posicion buscada
        aux = self.__comienzo
        encontrado = False
        dato = None
        if type(xpos) is int:
            if xpos < self.__tope:
                while aux != None and encontrado == False:
                    if aux.getPosicion() == xpos:
                        dato = aux.getDato()
                        encontrado = True
                    else:
                        aux = aux.getSiguiente()
        return dato

    def getIndice(self):
        return self.__indice

    def insertaAgente(self, unAparato, xpos):  ### Inciso 1
        encontrado = False
        if type(xpos) is int:
            aux = self.__comienzo
            anterior = aux
            if xpos < self.__tope:
                while aux != None and encontrado == False:
                    if aux.getPosicion() == xpos:
                        nodo = Nodo(unAparato, xpos)
                        anterior.setSiguiente(nodo)
                        aux.incrementaPosicion()
                        nodo.setSiguiente(aux)
                        encontrado = True
                        self.__tope += 1
                        print('Nodo insertado.')
                    else:
                        anterior = aux
                        aux = aux.getSiguiente()
                while aux != None and aux.getPosicion() < self.__tope:
                    aux.incrementaPosicion()
                    aux = aux.getSiguiente()
            else:
                print('La posicion dada supera el tope de la lista. No pudo insertarse.')