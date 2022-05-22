from claseCarrera import Carrera

class Facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''

    __listaCarreras = []
    def __init__(self,cod,nom,dire,loc,tel,listcarrera):
        if type(cod) is int:
            self.__codigo = cod
        else:
            print('Error de parametro codigo facultad.')
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = loc
        self.__telefono = tel
        self.__listaCarreras = []

        for i in range(len(listcarrera)):
            unaCarrera = Carrera(int(listcarrera[i][1]),listcarrera[i][2],listcarrera[i][4],listcarrera[i][3],listcarrera[i][5]) ### Se omite [i][0] porque es codigo de facultad
            self.__listaCarreras.append(unaCarrera)

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getCarreras(self):
        return self.__listaCarreras

    def getLocalidad(self):
        return self.__localidad