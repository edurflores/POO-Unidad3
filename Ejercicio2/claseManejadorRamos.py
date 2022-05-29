from claseRamo import Ramo

class ManejadorRamos:

    def __init__(self):
        self.__listaRamos = [] ### Ramos vendidos

    def agregaRamo(self,ramo):
        if type(ramo) is Ramo:
            self.__listaRamos.append(ramo)
        else:
            print('Error de parametro de clase ramo.')

    def creaRamo(self):
        print('Tamanhos de ramo disponibles')
        print('----------------')
        print('1- Chico.\n2- Mediano.\n3- Grande.')
        selec = input('Seleccione tamanho:')
        assert selec == '1' or '2' or '3', "Debe introducir 1, 2 o 3."
        tam = ''
        if selec == '1':
            tam = 'Chico'
        elif selec == '2':
            tam = 'Mediano'
        elif selec == '3':
            tam = 'Grande'
        unRamo = Ramo(tam)
        return unRamo

    def getFloresPorTamanio(self,xindice,xtam):
        if self.__listaRamos[xindice].getTamanio() == xtam:
            flores = self.__listaRamos[xindice].getFlores()
        else:
            flores = None
        return flores


    def getCantidadRamosVendidos(self):
        return len(self.__listaRamos)

    def retornaFlores(self,indice):
        return self.__listaRamos[indice].getFlores()