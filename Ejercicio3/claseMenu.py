from claseManejadorEquipos import ManejadorEquipos
from claseManejadorJugadores import ManejadorJugadores
from claseManejadorContratos import ManejadorContratos


class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '0':self.salir
        }
        self.__me = ManejadorEquipos()
        self.__mj = ManejadorJugadores()
        self.__mc = ManejadorContratos()
        self.__me.testEquipos()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        unjugador = self.__mj.RegistraJugador() ### Se crea al jugador y se lo guarda en la coleccion de jugadores
        equip = input('Ingrese equipo al que fue contratado:')
        indice = self.__me.buscaEquipo(equip)
        if indice != -1: ### Se ha encontrado al equipo en el arreglo de equipos
            uncontrato = self.__me.inscribeJugador(unjugador,indice) ### Se guarda el contrato del jugador en el equipo
            self.__mc.agregaContrato(uncontrato) ### Se guarda el contrato en la coleccion de contratos
            print('Se ha registrado el contrato del jugador.')
            print('------------------------------------')
        else:
            print('Error. Equipo no encontrado.')

    def opcion2(self):
        print('Consultar jugadores contratados.')
        print('------------------------------------')
        doc = input('Ingrese DNI del jugador a buscar:')
        indice = self.__mj.buscaJugadorDNI(doc)
        if indice != -1:
            self.__mc.muestraInfoContrato(doc)
            print('------------------------------------')
        else:
            print('Error. Jugador no encontrado.')

    def opcion3(self):
        nom = input('Ingrese nombre de equipo:')
        self.__me.muestraContratosAVencer(nom)

    def opcion4(self):
        nom = input('Ingrese nombre de equipo:')
        self.__me.ImporteContratos(nom)

    def opcion5(self):
        self.__mc.guardaArchivo()

    def salir(self):
        print('Salio del programa.')