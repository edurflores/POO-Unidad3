import datetime
class Contrato:
    __fechaInicio = ''
    __fechaFin = ''
    __pagomensual = 0.0

    __jugador = None
    __equipo = None

    def __init__(self,fechini,fechfin,pago,jug,equip):
        fechini = fechini.split('/')
        self.__fechaInicio = datetime.date(int(fechini[2]), int(fechini[1]), int(fechini[0]))
        fechfin = fechfin.split('/')
        self.__fechaFin = datetime.date(int(fechfin[2]), int(fechfin[1]), int(fechfin[0]))
        if type(pago) is float:
            self.__pagomensual = pago
        else:
            print('Error de parametro pago en Contrato.')

        self.__jugador = jug ### Objeto de clase jugador
        self.__equipo = equip ### Objeto de clase equipo

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFin(self):
        return self.__fechaFin

    def getPago(self):
        return self.__pagomensual