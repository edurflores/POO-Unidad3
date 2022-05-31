import csv
import datetime
import numpy as np
from claseEquipo import Equipo
from claseContrato import Contrato


class ManejadorEquipos:
    __dimension = 0
    __incremento = 5
    __cantidad = 0

    def __init__(self,dimension=0):
        self.__arreEquipos = np.empty(dimension,dtype=Equipo)
        self.__dimension = dimension

    def agregaEquipo(self,unEquipo):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arreEquipos.resize(self.__dimension)
        self.__arreEquipos[self.__cantidad] = unEquipo
        self.__cantidad += 1


    def testEquipos(self):
        archivo = open('Equipos.csv')
        reader = csv.reader(archivo,delimiter=';')
        ban = True
        for fila in reader:
            if ban:
                self.__dimension = int(fila[0]) ### La primera linea es la cantidad de equipos
                self.__arreEquipos.resize(self.__dimension)
                ban = not ban
            else:
                unEquipo = Equipo(fila[0],fila[1])
                self.agregaEquipo(unEquipo)
        archivo.close()
        print('Se han cargado los equipos.')

    def buscaEquipo(self,xequip):
        i = 0
        result = -1 ### No encontrado
        while i < len(self.__arreEquipos) and result == -1:
            if self.__arreEquipos[i].getNombre() == xequip:
                result = i
            else:
                i += 1
        return result

    def inscribeJugador(self,jugador,xindice):
        fecinicio = input('Ingrese fecha de inicio de contrato en formato dd/mm/aaaa:')
        fecfin = input('Ingrese fecha de inicio de contrato en formato dd/mm/aaaa:')
        pago = float(input('Ingrese pago mensual:'))
        uncontrato = Contrato(fecinicio,fecfin,pago,jugador,self.__arreEquipos[xindice])
        self.__arreEquipos[xindice].registraContrato(uncontrato)
        return uncontrato

    def muestraContratosAVencer(self,xequipo):
        indice = self.buscaEquipo(xequipo)
        if indice != -1:
            contratos = self.__arreEquipos[indice].getContratos()
            fechahoy = datetime.date.today()
            for i in range(len(contratos)):
                if contratos[i].getFechaFin() < fechahoy: ### Hace que compruebe la fecha menor a 6 meses
                    print(contratos[i].getJugador())
                    print('------------------------------------')

    def ImporteContratos(self,xequipo):
        acum = 0
        indice = self.buscaEquipo(xequipo)
        if indice != -1:
            contratos = self.__arreEquipos[indice].getContratos()
            for i in range(len(contratos)):
                acum += contratos[i].getPago()
            print('Importe total de los contratos del equipo %s: %.2f' % (self.__arreEquipos[indice].getNombre(),acum))
            print('------------------------------------')
        else:
            print('Error. Equipo no encontrado.')