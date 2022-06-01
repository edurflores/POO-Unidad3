from claseManejadorCalefactores import ManejadorCalefactores

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        n = int(input('Ingrese tamanio del arreglo de calefactores (numero entero positivo):'))
        self.__mc = ManejadorCalefactores(n)
        self.__mc.CargaCalGas()
        self.__mc.cargaCalElectrico()


    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        costo = int(input('Ingrese costo de metro cubico:'))
        cant = int(input('Ingrese cantidad que se estima consumir por metro cubico:'))
        self.__mc.buscaGasMenorConsumo(costo,cant)

    def opcion2(self):
        costo = int(input('Ingrese costo de kilowatt/h:'))
        cant = int(input('Ingrese cantidad que se estima consumir por hora:'))
        self.__mc.buscaElectricoMenorConsumo(costo,cant)

    def opcion3(self):
        self.__mc.MuestraMenorConsumo()

    def salir(self):
        print('Salio del programa.')