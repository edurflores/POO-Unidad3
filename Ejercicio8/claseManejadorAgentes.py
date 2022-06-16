from zope.interface import implementer
from Interfaces import IPrueba
from claseLista import Lista
from clasePersonal import Personal
from claseDocente import Docente
from claseApoyo import Apoyo
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseInterfaceTesorero import ITesorero ### Interfaces que restringen funciones miembro
from claseInterfaceDirector import IDirector


@implementer(IPrueba)
@implementer(ITesorero)
@implementer(IDirector)
class ManejadorAgentes:
    __listaAgentes = None

    def __init__(self):
        self.__listaAgentes = Lista()

    def agregarAgente(self,unagente): ### Inciso 2
        self.__listaAgentes.agregarPersona(unagente)
        print('Se agrego el agente.')

    def cargaDocente(self):
        print('Cargue los datos de un docente.')
        cuil = input('Ingrese CUIL:')
        ape = input('Ingrese apellido:')
        nom = input('Ingrese nombre:')
        ban = False ### Bandera para asegurar ingreso de un valor valido.
        while not ban:
            try:
                sueldo = float(input('Ingrese sueldo basico (entero o decimal):'))
                assert type(sueldo) is float, "Debe ser un numero entero o decimal."
                assert sueldo > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                anti = int(input('Ingrese antiguedad (en anios, numero entero):'))
                assert type(anti) is int, "Debe ser un numero entero."
                assert anti > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        carrera = input('Ingrese carrera:')
        ban = False
        while not ban:
            try:
                cargo = input('Ingrese cargo (simple, semiexclusivo, exclusivo):')
                cargo = cargo.lower()
                assert cargo == 'simple' or cargo == 'semiexclusivo' or cargo == 'exclusivo', "Solo puede ser simple, semiexclusivo o exclusivo."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        catedra = input('Ingrese catedra:')
        unDocente = Docente(cuil,ape,nom,sueldo,anti,carrera,cargo,catedra)
        return unDocente

    def cargaApoyo(self):
        print('Cargue los datos de un personal de apoyo.')
        cuil = input('Ingrese CUIL:')
        ape = input('Ingrese apellido:')
        nom = input('Ingrese nombre:')
        ban = False  ### Bandera para asegurar ingreso de un valor valido.
        while not ban:
            try:
                sueldo = float(input('Ingrese sueldo basico (entero o decimal):'))
                assert type(sueldo) is float, "Debe ser un numero entero o decimal."
                assert sueldo > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                anti = int(input('Ingrese antiguedad (en anios, numero entero):'))
                assert type(anti) is int, "Debe ser un numero entero."
                assert anti > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                categoria = int(input('Ingrese categoria (numero de 1 a 22):'))
                assert type(categoria) is int, "Debe ser un numero entero."
                assert categoria >= 1 and categoria <= 22, "Debe ser numero de 1 a 22."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        unApoyo = Apoyo(cuil,ape,nom,sueldo,anti,categoria)
        return unApoyo

    def cargaInvestigador(self):
        print('Cargue los datos de un investigador.')
        cuil = input('Ingrese CUIL:')
        ape = input('Ingrese apellido:')
        nom = input('Ingrese nombre:')
        ban = False  ### Bandera para asegurar ingreso de un valor valido.
        while not ban:
            try:
                sueldo = float(input('Ingrese sueldo basico (entero o decimal):'))
                assert type(sueldo) is float, "Debe ser un numero entero o decimal."
                assert sueldo > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                anti = int(input('Ingrese antiguedad (en anios, numero entero):'))
                assert type(anti) is int, "Debe ser un numero entero."
                assert anti > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        area = input('Ingrese area de investigacion (Exactas, Naturales, Tecnologia, etc.):')
        tipoinve = input('Ingrese tipo de investigacion (Descriptiva, Cuantitativa, Experimental, etc.):')
        unInvestigador = Investigador(cuil,ape,nom,sueldo,anti,area,tipoinve)
        return unInvestigador

    def cargaDocenteInvestigador(self):
        print('Cargue los datos de un docente investigador.')
        cuil = input('Ingrese CUIL:')
        ape = input('Ingrese apellido:')
        nom = input('Ingrese nombre:')
        ban = False  ### Bandera para asegurar ingreso de un valor valido.
        while not ban:
            try:
                sueldo = float(input('Ingrese sueldo basico (entero o decimal):'))
                assert type(sueldo) is float, "Debe ser un numero entero o decimal."
                assert sueldo > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                anti = int(input('Ingrese antiguedad (en anios, numero entero):'))
                assert type(anti) is int, "Debe ser un numero entero."
                assert anti > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        carrera = input('Ingrese carrera:')
        ban = False
        while not ban:
            try:
                cargo = input('Ingrese cargo (simple, semiexclusivo, exclusivo):')
                cargo = cargo.lower()
                assert cargo == 'simple' or cargo == 'semiexclusivo' or cargo == 'exclusivo', "Solo puede ser simple, semiexclusivo o exclusivo."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        catedra = input('Ingrese catedra:')
        area = input('Ingrese area de investigacion (Exactas, Naturales, Tecnologia, etc.):')
        tipoinve = input('Ingrese tipo de investigacion (Descriptiva, Cuantitativa, Experimental, etc.):')
        ban = False
        while not ban:
            try:
                cateincentivos = input('Ingrese categoria en el programa de incentivos (I, II, III, IV, V):')
                cateincentivos = cateincentivos.upper()
                assert len(cateincentivos) <= 3, "Tres caracteres como mucho."
                assert cateincentivos == 'I' or cateincentivos == 'II' or cateincentivos == 'III' or cateincentivos == 'IV' or cateincentivos == 'V'
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                impextra = float(input('Ingrese importe extra por docencia e investigacion (numero entero o decimal):'))
                assert type(impextra) is float, "Debe ser un numero entero o decimal."
                assert impextra > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        unDocenteInvestigador = DocenteInvestigador(cuil,ape,nom,sueldo,anti,carrera,cargo,catedra,area,tipoinve,cateincentivos,impextra)
        return unDocenteInvestigador

    def cargaunAgente(self): ### Inciso 2
        print('Carga de un agente.')
        print('1- Docente. 2- Investigador. 3- Apoyo. 4- Docente investigador.')
        ban = False
        while not ban:
            try:
                tipo = int(input('Seleccione tipo de agente a cargar:'))
                assert type(tipo) is int, "Debe ser un numero entero."
                assert tipo >= 1 and tipo <= 4, "Debe ser un numero de 1 a 4."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        if tipo == 1:
            unagente = self.cargaDocente()
            print('Se cargaron los datos de un docente.')
        elif tipo == 2:
            unagente = self.cargaInvestigador()
            print('Se cargaron los datos de un investigador.')
        elif tipo == 3:
            unagente = self.cargaApoyo()
            print('Se cargaron los datos de un personal de apoyo.')
        elif tipo == 4:
            unagente = self.cargaDocenteInvestigador()
            print('Se cargaron los datos de un docente investigador.')
        return unagente

    def insertarElemento(self,elem,xpos): ### Implementacion de interface Inciso 1.
        if type(xpos) is int:
            self.__listaAgentes.insertaAgente(elem, xpos - 1)

    def agregarElemento(self,elem): ### Implementacion de interface Inciso 2.
        self.__listaAgentes.agregarPersona(elem)
        print('Se ha agregado el agente.')


    def mostrarElemento(self,xpos): ### Implementacion de interface Inciso 3.
        agente = self.__listaAgentes.buscaPosicion(xpos)
        if agente.__class__.__name__ == 'DocenteInvestigador':
            print('En esta posicion hay un docente investigador.')
        elif agente.__class__.__name__ == 'Apoyo':
            print('En esta posicion hay un personal de apoyo.')
        elif agente.__class__.__name__ == 'Investigador':
            print('En esta posicion hay un investigador.')
        elif agente.__class__.__name__ == 'Docente':
            print('En esta posicion hay un docente.')
        else:
            print('No hay agente registrado en esta posicion.')

    def ordenaporApellido(self,xlista):
        xlista.sort(reverse=True)
        return xlista

    def ListaDocentesInvestigadoresCarrera(self,xcarrera): ### Inciso 4
        lista = []
        for agente in self.__listaAgentes:
            if isinstance(agente,DocenteInvestigador):
                if agente.getCarrera().lower() == xcarrera.lower():
                    lista.append(agente)
        lista = self.ordenaporApellido(lista)
        print('Nombre   Apellido      CUIL        Area de investigacion')
        for i in range(len(lista)):
            print('%s   %s  %s\t\t%s' % (lista[i].getNombre(),lista[i].getApellido(),lista[i].getCuil(),lista[i].getArea()))

    def cuentaAgentesArea(self,xarea): ### Inciso 5
        cont=[0,0] ## Contador de DocenteInvestigador / Investigador
        for agente in self.__listaAgentes:
                if isinstance(agente,DocenteInvestigador):
                    if agente.getArea().lower() == xarea.lower():
                        cont[0] += 1
                elif isinstance(agente,Investigador):
                    if agente.getArea().lower() == xarea.lower():
                        cont[1] += 1
        print('Docentes investigadores: {}'.format(cont[0]))
        print('Investigadores: {}'.format(cont[1]))

    def listadoSueldos(self): ### Inciso 6
        lista = []
        for agente in self.__listaAgentes:
            lista.append(agente)
        lista = self.ordenaporApellido(lista)
        print('Nombre   Apellido    Tipo de Agente     Sueldo')
        print('--------------------------------------------------')
        for i in range(len(lista)):
            if isinstance(lista[i],Docente):
                tipoagente = 'Docente'
            elif isinstance(lista[i],Investigador):
                tipoagente = 'Investigador'
            elif isinstance(lista[i],Apoyo):
                tipoagente = 'Apoyo'
            elif isinstance(lista[i],DocenteInvestigador):
                tipoagente = 'Docente investigador'
            print('%s   %s  \t%s\t\t\t%.2f' % (lista[i].getNombre(),lista[i].getApellido(),tipoagente,lista[i].calculaSueldo()))

    def listadoDocentesInvestigadores(self,xcat): ### Inciso 7
        total = 0
        print('Listado de docentes investigadores en la categoria {}'.format(xcat))
        print('-----------------------------------------------------------')
        print('Apellido    Nombre   Importe extra')
        print('----------------------------------')
        for agente in self.__listaAgentes:
            if isinstance(agente,DocenteInvestigador):
                if agente.getCategoriaIncentivos() == xcat:
                    print('%s   %s  \t%.2f' % (agente.getApellido(),agente.getNombre(),agente.getImporteExtra()))
                    total += agente.getImporteExtra()
        print('----------------------------------')
        print('Total a solicitar al Ministerio en concepto de importe extra en esta categoria: $%.2f' % (total))

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            agentes=[agente.toJSON() for agente in self.__listaAgentes]
        )
        return d

    ### Metodos para interfaces con restricciones

    def gastosSueldoPorEmpleado(self, dni): ### ITesorero
        terminar = False
        while not terminar:
            try:
                agente = next(self.__listaAgentes)
                if agente.getCuil() == dni:
                    terminar = True
                    print('Agente encontrado.')
                    print('Gastos de sueldo para este agente: $%.2f' % (agente.calculaSueldo()))
            except StopIteration:
                terminar = True
                print('No se encontro agente con el DNI solicitado.')

    def modificarBasico(self, dni, nuevoBasico): ### IDirector
        terminar = False
        while not terminar:
            try:
                agente = next(self.__listaAgentes)
                if agente.getCuil() == dni:
                    terminar = True
                    print('Agente encontrado.')
                    agente.setSueldoBasico(nuevoBasico)
                    print('Nuevo sueldo basico: $%.2f' % (agente.getSueldoBasico()))
            except StopIteration:
                terminar = True
                print('No se encontro agente con el DNI solicitado.')

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje): ### IDirector
        terminar = False
        while not terminar:
            try:
                agente = next(self.__listaAgentes)
                if agente.getCuil() == dni:
                    terminar = True
                    print('Agente encontrado.')
                    if isinstance(agente,Docente):
                        agente.setPorcentajeporCargo(nuevoPorcentaje)
                    else:
                        print('Error, este agente no es Docente. No aplica hacer esta modificacion.')
            except StopIteration:
                terminar = True
                print('No se encontro agente con el DNI solicitado.')

    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje): ### IDirector
        terminar = False
        while not terminar:
            try:
                agente = next(self.__listaAgentes)
                if agente.getCuil() == dni:
                    terminar = True
                    print('Agente encontrado.')
                    if isinstance(agente, Apoyo):
                        agente.setPorcentajeporCategoria(nuevoPorcentaje)
                    else:
                        print('Error, este agente no es personal de apoyo. No aplica hacer esta modificacion.')
            except StopIteration:
                terminar = True
                print('No se encontro agente con el DNI solicitado.')

    def modificarImporteExtra(self, dni, nuevoImporteExtra): ### IDirector
        terminar = False
        while not terminar:
            try:
                agente = next(self.__listaAgentes)
                if agente.getCuil() == dni:
                    terminar = True
                    print('Agente encontrado.')
                    if isinstance(agente, DocenteInvestigador):
                        agente.setImporteExtra(nuevoImporteExtra)
                    else:
                        print('Error, este agente no es docente investigador. No aplica hacer esta modificacion.')
            except StopIteration:
                terminar = True
                print('No se encontro agente con el DNI solicitado.')
