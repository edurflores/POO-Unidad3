import csv
import datetime
import numpy as np
from claseContrato import Contrato

from claseEquipo import Equipo
from claseJugador import Jugador

class ManejadorContratos:

    __dimension = 0
    __incremento = 5
    __cantidad = 0

    __arreContratos = None

    def __init__(self,dimension=0):
        self.__arreContratos = np.empty(dimension,dtype=Contrato)
        self.__dimension = dimension

    def agregaContrato(self,uncontrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreContratos.resize(self.__dimension)
        self.__arreContratos[self.__cantidad] = uncontrato
        self.__cantidad += 1

    def buscaContratoDNI(self,xdoc):
        i = 0
        result = -1 ### No encontrado
        while i < len(self.__arreContratos) and result == -1:
            if type(self.__arreContratos[i]) is Contrato:
                if self.__arreContratos[i].getJugador().getDocumento() == xdoc:
                    result = i
                else:
                    i += 1
        return result

    def muestraInfoContrato(self,xdocu): ### Inciso d. 3)
        indice = self.buscaContratoDNI(xdocu)
        if indice != -1:
            print('Jugador contratado.')
            print('Equipo: {}'.format(self.__arreContratos[indice].getEquipo().getNombre()))
            print('Fecha de finalizacion del contrato: {}'.format(self.__arreContratos[indice].getFechaFin().strftime('%d/%m/%Y')))
        else:
            print('El jugador no esta contratado.')

    def guardaArchivo(self):
        archivo = open('contratos.csv','w') ### Crea archivo para escritura si no existe
        writer = csv.writer(archivo,delimiter=';')
        for i in range(len(self.__arreContratos)):
            if type(self.__arreContratos[i]) is Contrato:
                docu = self.__arreContratos[i].getJugador().getDocumento()
                equipo = self.__arreContratos[i].getEquipo().getNombre()
                feinicio = self.__arreContratos[i].getFechaInicio()
                fefin = self.__arreContratos[i].getFechaFin()
                p = self.__arreContratos[i].getPago()
                fila = [docu,equipo,feinicio.strftime('%d/%m/%Y'),fefin.strftime('%d/%m/%Y'),str(p)]
                writer.writerow(fila)
        archivo.close()
        print('Se ha guardado el archivo "contratos.csv".')
        print('------------------------------------')