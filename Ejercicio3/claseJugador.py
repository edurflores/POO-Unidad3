import datetime

class Jugador:
    __nombre = ''
    __dni = ''
    __ciudadNatal = ''
    __paisOrigen = ''
    __fechaNacimiento= ''

    def __init__(self,nom,docu,ciudad,pais,fechanac):
        self.__nombre = nom
        self.__dni = docu
        self.__ciudadNatal = ciudad
        self.__paisOrigen = pais
        fechanac = fechanac.split('/')
        self.__fechaNacimiento = datetime.date(int(fechanac[2]),int(fechanac[1]),int(fechanac[0]))

    def getDocumento(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def __str__(self):
        return 'Nombre: ' + self.__nombre + ' DNI: ' + self.__dni + ' Ciudad natal: ' + self.__ciudadNatal + ' Pais: ' + self.__paisOrigen