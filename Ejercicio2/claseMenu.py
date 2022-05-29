from claseManejadorFlores import ManejadorFlores
from claseManejadorRamos import ManejadorRamos

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__mf = ManejadorFlores()
        self.__mf.testFlores()
        self.__mr = ManejadorRamos()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        print('Venta de ramo')
        print('---------------------------')
        ramo = self.__mr.creaRamo()
        flor = self.__mf.creaFlor()
        cant = int(input('Ingrese cantidad de la flor seleccionada:'))
        assert cant != 0, "La cantidad no puede ser cero"
        ramo.agregarFlor(flor,cant)
        op = int(input('Ingrese cero si no desea agregar mas flores:'))
        while op != 0:
            flor = self.__mf.creaFlor()
            cant = int(input('Ingrese cantidad de la flor seleccionada:'))
            assert cant != 0, "La cantidad no puede ser cero"
            ramo.agregarFlor(flor, cant)
            op = int(input('Ingrese cero si no desea agregar mas flores:'))
        self.__mr.agregaRamo(ramo)
        print('Se ha registrado el ramo.')

    def opcion2(self):
        print('Flores mas vendidas.')
        canramos = self.__mr.getCantidadRamosVendidos()
        for i in range(canramos):
            flores = self.__mr.retornaFlores(i)
            self.__mf.acumulaFlores(flores)
        self.__mf.muestraFloresMasVendidas()

    def opcion3(self):
        tam = input('Ingrese tipo de ramo (Chico, Mediano,o Grande):')
        canramos = self.__mr.getCantidadRamosVendidos()
        print('Flores vendidas en ramos de tamanio {}'.format(tam))
        for i in range(canramos):
            flores = self.__mr.getFloresPorTamanio(i,tam)
            if flores != None:
                self.__mf.muestraFloresRamo(flores)


    def salir(self):
        print('Salio del programa.')