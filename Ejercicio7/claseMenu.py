from claseManejadorAgentes import ManejadorAgentes
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
            '9':self.opcion9,
            '0':self.salir
        }
        self.__jsonf = ObjectEncoder() ### Administracion de archivo JSON
        self.__ma = ManejadorAgentes()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion incorrecta.'))
        func()

    def opcion1(self):
        print('Pendiente.')

    def opcion2(self): ### Debera ser por interface
        self.__ma.cargaunAgente()
        print('----------------------------------')

    def opcion3(self):
        ban = False
        while not ban:
            try:
                pos = int(input('Ingrese posicion (numero entero mayor a cero):'))
                assert type(pos) is int, "Debe ser un numero entero."
                assert pos > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__ma.buscaTipoAgente(pos - 1)
        print('----------------------------------')

    def opcion4(self):
        carrera = input('Ingrese carrera:')
        print('Carrera solicitada: {}'.format(carrera))
        self.__ma.ListaDocentesInvestigadoresCarrera(carrera)
        print('-------------------------------------------------------------')

    def opcion5(self):
        area = input('Ingrese area de investigacion:')
        print('Area de investigacion solicitada: {}'.format(area))
        print('Cantidad de agentes encontrados.')
        print('----------------------------------')
        self.__ma.cuentaAgentesArea(area)
        print('----------------------------------')

    def opcion6(self):
        self.__ma.listadoSueldos()
        print('----------------------------------')

    def opcion7(self):
        ban = False
        cat=''
        while not ban:
            try:
                cat = input('Ingrese categoria de investigacion (I, II, III, IV, V):')
                cat = cat.upper()
                assert len(cat) <= 3, "Tres caracteres como mucho."
                assert cat == 'I' or cat == 'II' or cat == 'III' or cat == 'IV' or cat == 'V'
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        self.__ma.listadoDocentesInvestigadores(cat)
        print('----------------------------------')

    def opcion8(self):
        d = self.__ma.toJSON()
        self.__jsonf.guardarJSONArchivo(d,'personal.json')
        print('Se ha guardado el archivo JSON.')
        print('----------------------------------')

    def opcion9(self):
        diccionario = self.__jsonf.leerJSONArchivo('personal.json')
        self.__ma = self.__jsonf.decodificarDiccionario(diccionario)
        print('Se ha cargado el archivo JSON.')
        print('----------------------------------')

    def salir(self):
        print('Salio del programa.')
        print('----------------------------------')