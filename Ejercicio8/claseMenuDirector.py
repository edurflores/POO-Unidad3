from claseInterfaceDirector import IDirector
from claseManejadorAgentes import ManejadorAgentes

class MenuDirector:
    __switcher = ()

    def __init__(self, manejarDirector:IDirector):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '0':self.salir
        }
        self.__manejadorDirector = manejarDirector

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion incorrecta.'))
        func()

    def opcion1(self):
        print('Modificar sueldo basico de un agente.')
        docu = input('Ingrese DNI del agente:')
        ban = False
        nuevoBasico = 0
        while not ban:
            try:
                nuevoBasico = float(input('Ingrese nuevo sueldo basico (nuemero entero o decimal):'))
                assert type(nuevoBasico) is float, "Debe ser numero entero o decimal."
                assert nuevoBasico > 0, "Debe ser numero positivo mayor a cero."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__manejadorDirector.modificarBasico(docu,nuevoBasico)
        print('----------------------------------')

    def opcion2(self):
        print('Modificar porcentaje por cargo a un docente.')
        docu = input('Ingrese DNI del docente:')
        ban = False
        nuevoporcen = 0
        while not ban:
            try:
                nuevoporcen = int(input('Ingrese nuevo porcentaje (numero entero):'))
                assert type(nuevoporcen) is int, "Debe ser numero entero."
                assert nuevoporcen >= 0, "Debe ser numero mayor o igual a cero."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__manejadorDirector.modificarPorcentajeporcargo(docu,nuevoporcen)
        print('----------------------------------')

    def opcion3(self):
        print('Modificar porcentaje por categoria a un personal de apoyo.')
        docu = input('Ingrese DNI del personal de apoyo:')
        ban = False
        nuevoporcen = 0
        while not ban:
            try:
                nuevoporcen = int(input('Ingrese nuevo porcentaje (numero entero):'))
                assert type(nuevoporcen) is int, "Debe ser numero entero."
                assert nuevoporcen >= 0, "Debe ser numero mayor o igual a cero."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__manejadorDirector.modificarPorcentajeporcategoria(docu,nuevoporcen)
        print('----------------------------------')

    def opcion4(self):
        print('Modificar importe extra a un docente investigador.')
        docu = input('Ingrese DNI del docente investigador:')
        ban = False
        nuevoimporte = 0
        while not ban:
            try:
                nuevoimporte = float(input('Ingrese nuevo importe extra (numero entero o decimal):'))
                assert type(nuevoimporte) is float, "Debe ser numero entero o decimal."
                assert nuevoimporte >= 0, "Debe ser numero mayor o igual a cero."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__manejadorDirector.modificarImporteExtra(docu,nuevoimporte)
        print('----------------------------------')

    def salir(self):
        print('Salio del menu de director.')
        print('----------------------------------')