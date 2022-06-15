from Interfaces import IPrueba ### Interface del Ejercicio 5
from claseManejadorAparatos import ManejadorAparatos
from claseObjectEncoder import ObjectEncoder


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
            '7':self.opcion7,
            '8':self.opcion8,
            '0':self.salir
        }
        self.__jsonF = ObjectEncoder() ### Administracion de archivo JSON
        self.__ma = ManejadorAparatos() ### Manejador
        self.__interface = IPrueba(self.__ma)  ### Interface
        self.opcion8() ### Carga por primera vez el archivo JSON (eliminar si no hay archivo JSON o dara error)

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda: print('Error. Opcion incorrecta.'))
        func()

    def opcion1(self):
        ban = False  ### Bandera para asegurar ingreso de valor correcto.
        print('Insertar un aparato a la coleccion en una posicion determinada.')
        print('----------------------------------')
        print('1- Televisor. 2- Heladera. 3- Lavarropa.')
        while not ban:
            try:
                num = int(input('Ingrese numero de tipo de aparato a insertar:'))
                assert type(num) is int, "Debe ser un numero entero."
                assert num >= 1 and num <= 3, "Debe ser un numero de 1 a 3."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        aparato = self.__ma.cargaUnDispositivo(num)
        ban = False ### Bandera para asegurar ingreso de valor correcto.
        while not ban:
            try:
                posicion = int(input('Ingrese posicion (numero entero positivo): '))
                assert type(posicion) is int, "Debe ser un numero entero."
                assert posicion > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__interface.insertarElemento(aparato,posicion) ### Por interface
        print('----------------------------------')

    def opcion2(self):
        ban = False ### Bandera para asegurar ingreso de valor correcto.
        print('Agregar un aparato a la coleccion.')
        print('----------------------------------')
        print('1- Televisor. 2- Heladera. 3- Lavarropa.')
        while not ban:
            try:
                num = int(input('Ingrese numero de tipo de aparato a agregar:'))
                assert type(num) is int, 'Debe ser un numero entero.'
                assert num >= 1 and num <= 3, "Debe ser un numero de 1 a 3."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True ### Se introdujo un valor valido.
        aparato = self.__ma.creaAparato(num)
        self.__interface.agregarElemento(aparato) ### Por interface
        #### self.__ma.agregaUnAparato(aparato)
        print('----------------------------------')

    def opcion3(self):
        ban = False ### Bandera para asegurar ingreso de valor correcto.
        print('Informar tipo de objeto.')
        print('----------------------------------')
        while not ban:
            try:
                pos = int(input('Ingrese posicion de la lista (numero entero positivo): '))
                assert type(pos) is int, "Debe ser un numero entero."
                assert pos > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ### self.__ma.mostrarElemento(pos)
        self.__interface.mostrarElemento(pos)
        print('----------------------------------')

    def opcion4(self):
        self.__ma.informaAparatosPhillips()
        print('----------------------------------')

    def opcion5(self):
        self.__ma.MarcaLavarropasCargaSup()
        print('----------------------------------')

    def opcion6(self):
        self.__ma.MuestraAparatos()

    def opcion7(self):
        d = self.__ma.toJSON() ### Diccionario con los objetos a guardar en el archivo JSON
        self.__jsonF.guardarJSONArchivo(d,'aparatoselectronicos.json')
        print('Se ha guardado el archivo JSON.')
        print('----------------------------------')

    def opcion8(self):
        diccionario = self.__jsonF.leerJSONArchivo('aparatoselectronicos.json')
        self.__ma = self.__jsonF.decodificarDiccionario(diccionario)
        self.__interface = IPrueba(self.__ma)
        print('Se ha cargado el archivo JSON.')
        print('----------------------------------')

    def salir(self):
        print('Salio del programa.')