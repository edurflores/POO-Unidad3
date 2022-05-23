from claseManejadorFacultades import ManejadorFacultades

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
            }

        self.__mf = ManejadorFacultades()
        self.__mf.testFacultades()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error, opcion no valida.'))
        func()

    def salir(self):
        print('Salio del programa.')

    def opcion1(self):
        cod = int(input('Ingrese codigo de facultad:'))
        indice = self.__mf.buscaFacultad(cod)
        if indice != -1:
            self.__mf.muestraFacultad(indice)
        else:
            print('Error. Facultad no encontrada.')

    def opcion2(self):
        nomcar = input('Ingrese nombre de carrera:')
        ban = self.__mf.muestraCarrera(nomcar)
        if ban == False:
            print('Error. Carrera no encontrada.')

    def opcion3(self):
        cod = int(input('Ingrese codigo de facultad a borrar:'))
        indice = self.__mf.buscaFacultad(cod)
        if indice != -1:
            self.__mf.borraFacultad(indice)
        else:
            print('Error. Facultad no encontrada.')