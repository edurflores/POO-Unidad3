from claseManejadorAparatos import ManejadorAparatos

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '0':self.salir
        }

        self.__ma = ManejadorAparatos()
        self.__ma.testTelevisores()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda: print('Error. Opcion incorrecta.'))
        func()

    def opcion1(self):
        print('Insertar un aparato a la coleccion en una posicion determinada.')
        print('----------------------------------')
        print('1- Televisor. 2- Heladera. 3- Lavarropa.')
        num = int(input('Ingrese numero de tipo de aparato a insertar:'))
        aparato = self.__ma.cargaUnDispositivo(num)
        posicion = int(input('Ingrese posicion (numero entero positivo): '))
        self.__ma.insertaAparatoPosicion(aparato,posicion)
        print('----------------------------------')

    def opcion2(self):
        print('Agregar un aparato a la coleccion.')
        print('----------------------------------')
        print('1- Televisor. 2- Heladera. 3- Lavarropa.')
        num = int(input('Ingrese numero de tipo de aparato a agregar:'))
        aparato = self.__ma.cargaUnDispositivo(num)
        self.__ma.agregaUnAparato(aparato)
        print('----------------------------------')

    def opcion3(self):
        print('Informar tipo de objeto.')
        print('----------------------------------')
        pos = input('Ingrese posicion de la lista: ')

    def opcion4(self):
        self.__ma.informaAparatosPhillips()
        print('----------------------------------')

    def opcion5(self):
        self.__ma.MarcaLavarropasCargaSup()
        print('----------------------------------')

    def opcion6(self):
        self.__ma.MuestraAparatos()

    def salir(self):
        print('Salio del programa.')