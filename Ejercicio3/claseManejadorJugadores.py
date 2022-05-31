import datetime
from claseJugador import Jugador

class ManejadorJugadores:
    __listaJugadores = None
    def __init__(self):
        self.__listaJugadores = []

    def agregaJugador(self,unjugador):
        self.__listaJugadores.append(unjugador)

    def RegistraJugador(self):
        nom = input('Ingrese nombre:')
        docu = input('Ingrese DNI:')
        cnatal = input('Ingrese ciudad natal:')
        pais = input('Ingrese pais de origen:')
        fechnac = input('Ingrese fecha de nacimiento en formato dd/mm/aaaa:')
        unJugador = Jugador(nom,docu,cnatal,pais,fechnac)
        self.agregaJugador(unJugador) ### Agregado a la coleccion de
        print('Se ha guardado el jugador.')
        return unJugador

    def buscaJugadorDNI(self,xdoc):
        i = 0
        result = -1
        while i < len(self.__listaJugadores) and result == -1:
            if self.__listaJugadores[i].getDocumento() == xdoc:
                result = i
            else:
                i += 1
        return result