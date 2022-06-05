from zope.interface import implementer
from Interfaces import IPrueba

@implementer(IPrueba)
class ManejadorColeccion:
    __listaElementos = None

    def __init__(self):
        self.__listaElementos = []

    def insertarElemento(self,elem,xpos):
        try:
            self.__listaElementos[xpos - 1] = elem
        except:
            print('Error. El elemento no pudo insertarse en la posicion indicada.')

    def agregarElemento(self,elem):
        self.__listaElementos.append(elem)

    def mostrarElemento(self,xpos):
        try:
            print('Posicion: {}'.format(xpos))
            print('Elemento:')
            print(self.__listaElementos[xpos - 1])
            print('-------------------------')
        except:
            print('Error. No es posible mostrar el elemento.')

    def cargaElementos(self): ### Inicializa la lista con algunos datos.
        self.agregarElemento(3)
        self.agregarElemento(5)
        self.agregarElemento('Jose')
        self.agregarElemento('Argentina')
        self.agregarElemento(177.013)
        self.agregarElemento('Gambare')
        self.agregarElemento(94)
        print('Inicializado con algunos elementos.')