import csv
from claseFacultad import Facultad

class ManejadorFacultades:

    def __init__(self):
        self.__listaFacultades = []

    def agregaFacultad(self,facu):
        if type(facu) is Facultad:
            self.__listaFacultades.append(facu)
        else:
            print('Error de parametro, debe ser instancia de Facultad.')

    def testFacultades(self): ### Corregir esto, no es valido
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=';')
        ban = True
        listaCarreras = []  ### Lista auxiliar para almacenar lineas de las carreras
        facu = '' ### Variable auxiliar para almacenar la linea de facultad

        for fila in reader:
            if ban:
                facu = fila
                print(facu)
                print(fila)
                ban = not ban
            else:
                print(fila[0])
                print(facu[0])
                if fila[0] == facu[0]: ### Compara codigos para saber si seguimos en la misma facultad
                    listaCarreras.append(fila) ### Agrega linea con info de carreras
                else: ### Cambio de facultad, entonces se crea la instancia
                    nuevafacultad = Facultad(int(facu[0]),facu[1],facu[2],facu[3],facu[4],listaCarreras)
                    self.__listaFacultades.append(nuevafacultad)
                    facu = fila ### Se toma la siguiente facultad para reiniciar el proceso
                    print(facu)
                    listaCarreras.clear() ### Borra la lista para reiniciarla
        print('Se han cargado las facultades.')
        ### Nota del problema, no carga la ultima facultad porque nunca ejecuta el else, ya que siempre va a darse el fila[0] == facu[0]
    def buscaFacultad(self,xcod):
        i = 0
        ban = -1 ### No encontrado
        while i < len(self.__listaFacultades) and ban == -1:
            if self.__listaFacultades[i].getCodigo() == xcod:
                ban = i
            else:
                i += 1
        return ban

    def muestraFacultad(self,xindice):
        print('Nombre de facultad: {}'.format(self.__listaFacultades[xindice].getNombre()))
        print('Carreras.')
        print('---------------------------')
        lista = self.__listaFacultades[xindice].getCarreras()
        for i in range(len(lista)):
            print(lista[i])
        print('---------------------------')

    def muestraCarrera(self,xnom):
        i = 0
        j = 0
        ban = False ### No encontrada
        while i < len(self.__listaFacultades) and ban == False:
            while j < len(self.__listaFacultades[i].getCarreras()) and ban == False:
                if xnom in self.__listaFacultades[i].getCarreras()[j].getNombreCarrera():
                    print('Informacion de la carrera.')
                    print('--------------------------------')
                    print('Codigo: {} {}'.format(self.__listaFacultades[i].getCodigo(),self.__listaFacultades[i].getCarreras()[j].getCodiCarrera()))
                    print('Nombre: {}'.format(self.__listaFacultades[i].getCarreras()[j].getNombreCarrera()))
                    print('Localidad: {}'.format(self.__listaFacultades[i].getLocalidad()))
                    print('--------------------------------')
                    ban = True
                else:
                    j += 1
            i += 1
        return ban