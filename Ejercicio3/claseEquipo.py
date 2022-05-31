class Equipo:
    __nombre = ''
    __ciudad = ''

    __contratos = None

    def __init__(self,nom,ciu):
        self.__nombre = nom
        self.__ciudad = ciu

        self.__contratos = []

    def getNombre(self):
        return self.__nombre

    def registraContrato(self,uncontrato):
        self.__contratos.append(uncontrato)

    def getContratos(self):
        return self.__contratos