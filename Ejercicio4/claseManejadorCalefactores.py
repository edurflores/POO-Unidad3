import csv
import numpy as np
from claseCalefactor import Calefactor
from claseCalefactorGas import CalefactorGas
from claseCalefactorElectrico import CalefactorElectrico

class ManejadorCalefactores:
    __dimension = 0
    __cantidad = 0
    __incremento = 5
    __arreCalefactores = None

    def __init__(self,dimension=0):
        self.__arreCalefactores = np.empty(dimension,dtype=Calefactor)
        self.__dimension = dimension
        self.__dicconsumo = {} ### Diccionario que guarda pares calefactor/costo

    def agregaCalefactor(self,unCalefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreCalefactores.resize(self.__dimension)
        self.__arreCalefactores[self.__cantidad] = unCalefactor
        self.__cantidad += 1

    def cargaCalElectrico(self):
        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo,delimiter=';')
        ban = True
        for fila in reader:
            if ban:
                ban = not ban
            else:
                unCalElectrico = CalefactorElectrico(fila[0],fila[1],int(fila[2]))
                self.agregaCalefactor(unCalElectrico)
        archivo.close()
        print('Se han cargado los calefactores electricos.')

    def CargaCalGas(self):
        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo, delimiter=';')
        ban = True
        for fila in reader:
            if ban:
                ban = not ban
            else:
                unCalGas = CalefactorGas(fila[0],fila[1],fila[2],int(fila[3]))
                self.agregaCalefactor(unCalGas)
        archivo.close()
        print('Se han cargado los calefactores a gas.')

    def buscaGasMenorConsumo(self,xcost,xcant):
        for i in range(len(self.__arreCalefactores)):
            if isinstance(self.__arreCalefactores[i],CalefactorGas):
                cost = (self.__arreCalefactores[i].getCalorias() / 1000) * xcant * xcost ### Calcula consumo $
                self.__dicconsumo[self.__arreCalefactores[i]] = cost
        listaconsumo = sorted(self.__dicconsumo.items(),key=lambda x:x[1])
        print('Calefactor a gas de menor consumo.')
        print('-------------------------------')
        j = 0
        ban = False
        while j < len(listaconsumo) and ban == False:
            if isinstance(listaconsumo[j][0],CalefactorGas):
                print('Marca: {}'.format(listaconsumo[j][0].getMarca())) ### La primera componente encontrada de la lista ordenada es la de menor consumo
                print('Modelo: {}'.format(listaconsumo[j][0].getModelo()))
                print('Costo: $ %.2f' % (listaconsumo[j][1]))
                print('-------------------------------')
                ban = True ### Sale del bucle
            else:
                j += 1
        listaconsumo.clear()

    def buscaElectricoMenorConsumo(self,xcost,xcant):
        for i in range(len(self.__arreCalefactores)):
            if isinstance(self.__arreCalefactores[i],CalefactorElectrico):
                cost = (self.__arreCalefactores[i].getPotencia() / 1000) * xcant * xcost ### Calcula consumo $
                self.__dicconsumo[self.__arreCalefactores[i]] = cost
        listaconsumo = sorted(self.__dicconsumo.items(),key=lambda x:x[1])
        print('Calefactor electrico de menor consumo.')
        print('-------------------------------')
        j = 0
        ban = False
        while j < len(listaconsumo) and ban == False:
            if isinstance(listaconsumo[j][0], CalefactorElectrico):
                print('Marca: {}'.format(listaconsumo[j][0].getMarca()))  ### La primera componente encontrada de la lista ordenada es la de menor consumo
                print('Modelo: {}'.format(listaconsumo[j][0].getModelo()))
                print('Costo: $ %.2f' % (listaconsumo[j][1]))
                print('-------------------------------')
                ban = True  ### Sale del bucle
            else:
                j += 1
        listaconsumo.clear()

    def MuestraMenorConsumo(self):
        listconsumo = sorted(self.__dicconsumo.items(),key=lambda x:x[1])
        print('Calefactor de menor consumo.')
        print('-------------------------------')
        if isinstance(listconsumo[0][0],CalefactorElectrico):
            print('Tipo de calefactor: Electrico.')
        if isinstance(listconsumo[0][0],CalefactorGas):
            print('Tipo de calefactor: Gas.')
        print('Marca: {}'.format(listconsumo[0][0].getMarca()))
        print('Modelo: {}'.format(listconsumo[0][0].getModelo()))
        print('Costo: $ %.2f' % (listconsumo[0][1]))
        print('-------------------------------')
        listconsumo.clear()