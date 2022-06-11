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

    def agregarAparato(self,unaparato):
        nodo = Nodo(unaparato,self.__numeronodo)
        self.__numeronodo += 1
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertaAparato(self,unAparato,xpos): ### Inserta un aparato en una posicion valida determinada
        if type(xpos) is int:
            if self.__tope == 0: ### La lista esta vacia. Se lo inserta al principio.
                print('Lista vacia detectada. Se hara insercion al principio.')
                nodo = Nodo(unAparato,0)
                self.__numeronodo += 1
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
                self.__actual = nodo
                self.__tope += 1
                print('Se ha insertado el nodo al principio de la lista. Se ignoro posicion dada por el usuario.')
            elif xpos < self.__tope: ### La lista no esta vacia. Se hara insercion en la posicion solicitada.
                    nodo = Nodo(unAparato,xpos)
                    nodo.setSiguiente(self.__comienzo)
                    aux = self.__comienzo ### Se resguarda la lista de las modificaciones
                    anterior = nodo ### Para hacer insercion adentro o al final.
                    while aux != None and nodo.getPosicion() < xpos: ### Recorrido
                        anterior = aux
                        aux = aux.getSiguiente()
                    anterior.setSiguiente(nodo) ### Se inserta el nuevo nodo en el medio
                    nodo.setSiguiente(aux)
                    while aux != None: ### Incrementa en 1 la posicion de los nodos que siguen
                        aux.incrementaPosicion()
                        aux = aux.getSiguiente()
                    self.__tope += 1 ### Al insertarse un nodo mas, se incrementa el total de nodos
                    print('Nodo insertado.')

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


    def listarDatosAparatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    ### Sigue funcion eliminar por x pero parece que no es tan necesaria
