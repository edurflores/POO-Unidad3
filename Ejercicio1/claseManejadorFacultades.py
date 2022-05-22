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

    def testFacultades(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=';')
        ban = True
        lineasCarreras = []  ### Lista auxiliar para almacenar lineas de las carreras
        facu = next(reader) ### Variable auxiliar que almacena la linea con informacion de la facultad
        while ban:
            linea = next(reader) ### Se pasa al siguiente para tomar la primera carrera
            while ban and facu[0] == linea[0]:
                lineasCarreras.append(linea)
                try:
                    linea = next(reader)
                except StopIteration:
                    ban = False
            unaFacultad = Facultad(int(facu[0]),facu[1],facu[2],facu[3],facu[4],lineasCarreras) ### Crea la facultad
            self.agregaFacultad(unaFacultad)
            lineasCarreras.clear() ### Reinicia lista de lineas de carreras
            facu = linea ### La linea corresponde a una nueva facultad
        archivo.close()
        print('Se han cargado las facultades.')
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
            carreras = self.__listaFacultades[i].getCarreras()
            while j < len(carreras) and ban == False:
                if xnom.lower() in carreras[j].getNombreCarrera().lower():
                    print('Informacion de la carrera.')
                    print('--------------------------------')
                    print('Codigo: {} {}'.format(self.__listaFacultades[i].getCodigo(),carreras[j].getCodiCarrera()))
                    print('Nombre: {}'.format(carreras[j].getNombreCarrera()))
                    print('Localidad: {}'.format(self.__listaFacultades[i].getLocalidad()))
                    print('--------------------------------')
                    ban = True
                else:
                    j += 1
            i += 1
            j = 0
        return ban
