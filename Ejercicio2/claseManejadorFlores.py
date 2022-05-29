import csv
import numpy as np
from claseFlor import Flor

class ManejadorFlores:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=0, incremento=5):
        self.__arreFlores = np.empty(dimension,dtype=Flor)
        self.__cantidad = 0
        self.__dimension = dimension


    def agregaFlor(self,flor):
        if type(flor) is Flor:
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__arreFlores.resize(self.__dimension)
            self.__arreFlores[self.__cantidad] = flor
            self.__cantidad += 1
        else:
            print('Error de parametro de clase Flor.')

    def testFlores(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unaflor = Flor(int(fila[0]),fila[1])
                self.agregaFlor(unaflor)
        archivo.close()
        print('Se han cargado las flores.')

    def muestraflores(self):
        for i in range(len(self.__arreFlores)):
            if type(self.__arreFlores[i]) is Flor:
                print(self.__arreFlores[i])

    def buscaFlor(self,f):
        result = -1 ### No encontrada
        i = 0
        while i < len(self.__arreFlores) and result == -1:
            if type(self.__arreFlores[i]) is Flor:
                if f == self.__arreFlores[i].getNumero():
                    result = i
                else:
                    i += 1
        return result

    def creaFlor(self):
        print('Flores disponibles')
        print('---------------------------')
        self.muestraflores()
        flor = int(input('Ingrese numero de la flor deseada:'))
        indice = self.buscaFlor(flor)
        assert indice != -1, "Error. Flor no disponible."
        print('Colores disponibles: blanco, rojo, rosa, amarillo, violeta.')
        col = input('Ingrese color deseado:')
        assert col == 'blanco' or 'rojo' or 'rosa' or 'amarillo' or 'violeta', "Error. Color no disponible"
        unaFlor = Flor(self.__arreFlores[indice].getNumero(),
                       self.__arreFlores[indice].getNombre(), col)
        return unaFlor

    def acumulaFlores(self,xflores): ### flores es lista conteniendo objetos de clase Flor
        self.__acumulador = np.zeros(self.__dimension, dtype=int)  ### Acumulador de flores vendidas inicializado en cero
        for i in range(len(xflores)):
            num = xflores[i].getNumero() ### Numero de flor, coincide con el indice - 1 del acumulador
            self.__acumulador[num - 1] += 1

    def muestraFloresMasVendidas(self):
        dicmasvendidas = dict()  ### pares nombreflor/cantidad vendida
        for i in range(len(self.__acumulador)):
            dicmasvendidas[self.__arreFlores[i].getNombre()] = self.__acumulador[i]

        print('Cantidad de flores vendidas.')
        print('-------------------------')
        print('Nombre     Cantidad')
        for i in range(len(self.__acumulador)):
            dicmasvendidas[self.__arreFlores[i].getNombre()] = self.__acumulador[i]
        for nom, val in sorted(dicmasvendidas.items(),key=lambda x:x[1], reverse=True):
            print('{}       {} '.format(nom,val))

    ### dic.items() convierte al diccionario en una lista cuyas componentes son los pares clave:valor. Sorted ordena el diccionario, key=lambda x:x[1] configura para que ordene segun valor
    ### reverse=True configura para que ordene en orden descendente (mayor a menor)

    def muestraFloresRamo(self,xflores): ### Para inciso 3
        print('Numero   Nombre     Descripcion')
        nom = xflores[0].getNombre()
        ban = True
        for i in range(len(xflores)):
            if ban: ### Para que lo coloque una vez
                print('{}   \t{}\t   {}'.format(xflores[i].getNumero(),xflores[i].getNombre(),xflores[i].getDescripcion()))
                ban = not ban
            else:
                if xflores[i].getNombre() != nom:
                    nom = xflores[i].getNombre()
                    ban = True

        print('----------------------------------')