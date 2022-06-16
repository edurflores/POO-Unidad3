from zope.interface import Interface

class IPrueba(Interface):

    def insertarElemento(self,elem,xpos): ### Inciso 1
        pass

    def agregarElemento(self,elem): ### Inciso 2
        pass

    def mostrarElemento(self,xpos): ### Inciso 3
        pass
