class Personal:
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldobasico = 0.0
    __antiguedad = ''

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera='',cargo='',catedra='',categoria=0,area='',tipoinvestigacion='',categoriaincentivos='',importeextra=0):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        if type(sueldobasico) is float:
            self.__sueldobasico = sueldobasico
        else:
            print('Error de parametro sueldo basico en Personal.')
        if type(antiguedad) is int:
            self.__antiguedad = antiguedad
        else:
            print('Error de parametro antiguedad en Personal. Debe ser int.')

    def toJSON(self):
        pass

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldobasico

    def getAntiguedad(self):
        return self.__antiguedad

    def calculaSueldo(self):
        pass

    def __lt__(self, otroagente): ### Para permitir ordenar por apellido
        if self.__apellido > otroagente.getApellido():
            result = True
        else:
            result = False
        return result