class Carrera:
    __codigo = 0
    __nombre = ''
    __duracion = ''
    __titulo = ''
    __tipo = '' ### Grado, pregrado, etc.

    def __init__(self,cod,nom,dur,tit,tip):
        if type(cod) is int:
            self.__codigo = cod
        else:
            print('Error de parametro codigo.')
        self.__nombre = nom
        self.__duracion = dur
        self.__titulo = tit
        self.__tipo = tip

    def getNombreCarrera(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getCodiCarrera(self):
        return self.__codigo

    def __str__(self):
        return 'Nombre: ' + self.__nombre + ' | Duracion: ' + self.__duracion