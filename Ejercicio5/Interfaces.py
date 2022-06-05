from zope.interface import Interface

class IPrueba(Interface):

    def insertarElemento(self,elem,xpos):
        pass

    def agregarElemento(self,elem):
        pass

    def mostrarElemento(self,xpos):
        pass
