from zope.interface import implementer
from Interfaces import IPrueba
from claseAparato import Aparato
from claseTelevisor import Televisor
from claseHeladera import Heladera
from claseLavarropa import Lavarropa

from claseLista import Lista

@implementer(IPrueba)
class ManejadorAparatos:
    __listaAparatos = None

    def __init__(self):
        self.__listaAparatos = Lista()

    def cargaUnTelevisor(self):
        ban = False  ### Bandera para asegurar ingreso de valor correcto.
        print('Ingrese los datos del televisor.')
        print('----------------------------------')
        marc = input('Ingrese marca: ')
        mod = input('Ingrese modelo: ')
        col = input('Ingrese color: ')
        pais = input('Ingrese pais de fabricacion: ')
        while not ban:
            try:
                precio = float(input('Ingrese precio base: '))
                assert type(precio) is float, "Debe ingresar un numero entero o decimal."
                assert precio >= 0, "No puede ingresar numeros negativos."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        tipopant = input('Ingrese tipo de pantalla (CRT, VGA, SVGA, Plasma, LCD, LED, TouchScreen, MultiTouch): ')
        ban = False
        while not ban:
            try:
                pulg = int(input('Ingrese cantidad de pulgadas (numero entero): '))
                assert type(pulg) is int, "Debe ser un numero entero."
                assert pulg > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                tdef = input('Ingrese tipo de definicion (SD, HD, FULL HD): ')
                tdef = tdef.upper()
                assert tdef == 'SD' or tdef == 'HD' or tdef == 'FULL HD', "Solo puede ser SD, HD o FULL HD."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                conex = int(input('Indique si tiene conexion a internet (1- Si. 2- No.): '))
                assert type(conex) is int, "Debe ser un numero entero."
                assert conex == 1 or conex == 2, "Debe ser 1 o 2."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        if conex == 1:
            conex = True
        else:
            conex = False
        unTelevisor = Televisor(marc,mod,col,pais,precio,tipopant,pulg,tdef,conex)
        return unTelevisor

    def cargaUnaHeladera(self):
        ban = False  ### Bandera para asegurar ingreso de valor correcto.
        print('Ingrese los datos de la heladera.')
        print('----------------------------------')
        marc = input('Ingrese marca: ')
        mod = input('Ingrese modelo: ')
        col = input('Ingrese color: ')
        pais = input('Ingrese pais de fabricacion: ')
        while not ban:
            try:
                precio = float(input('Ingrese precio base: '))
                assert type(precio) is float, "Debe ingresar un numero entero o decimal."
                assert precio >= 0, "No puede ingresar numeros negativos."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                cap = int(input('Ingrese capacidad en litros (numero entero): '))
                assert type(cap) is int, "Debe ingresar un numero entero."
                assert cap > 0, "Debe ser un numero positivo."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                frez = int(input('Indique si tiene freezer (1- Si. 2- No.): '))
                assert type(frez) is int, "Debe ser un numero entero."
                assert frez == 1 or frez == 2, "Debe ser 1 o 2."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        if frez == 1:
            frez = True
        else:
            frez = False
        ban = False
        while not ban:
            try:
                cic = int(input('Indique si es ciclica (1- Si. 2- No.): '))
                assert type(cic) is int, "Debe ser un numero entero."
                assert cic == 1 or cic == 2, "Debe ser 1 o 2."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        if cic == 1:
            cic = True
        else:
            cic = False
        unaHeladera = Heladera(marc,mod,col,pais,precio,cap,frez,cic)
        return unaHeladera

    def cargaUnLavarropa(self):
        ban = False  ### Bandera para asegurar ingreso de valor correcto.
        print('Ingrese los datos del lavarropa.')
        print('----------------------------------')
        marc = input('Ingrese marca: ')
        mod = input('Ingrese modelo: ')
        col = input('Ingrese color: ')
        pais = input('Ingrese pais de fabricacion: ')
        while not ban:
            try:
                precio = float(input('Ingrese precio base: '))
                assert type(precio) is float, "Debe ingresar un numero entero o decimal."
                assert precio >= 0, "No puede ingresar numeros negativos."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                caplav = int(input('Ingrese capacidad de lavado kg (numero entero): '))
                assert type(caplav) is int, "Debe ingresar un numero entero."
                assert caplav > 0, "Debe ingresar un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                vel = int(input('Ingrese velocidad de centrifugado rpm (numero entero): '))
                assert type(vel) is int, "Debe ingresar un numero entero."
                assert vel > 0, "Debe ingresar un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                cantpr = int(input('Ingrese cantidad de programas (numero entero): '))
                assert type(cantpr) is int, "Debe ingresar un numero entero."
                assert cantpr > 0, "Debe ingresar un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        ban = False
        while not ban:
            try:
                tipocar = input('Ingrese tipo de carga (Frontal, Superior): ')
                tipocar = tipocar.lower()
                assert tipocar == 'frontal' or tipocar == 'superior', "Solo puede optarse por Frontal o Superior."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        unLavarropa = Lavarropa(marc,mod,col,pais,precio,caplav,vel,cantpr,tipocar)
        return unLavarropa

    def creaAparato(self,xtipo): ### Carga un dispositivo (inciso 2)
        ### disp es variable que guarda el objeto dispositivo (televisor, heladera o lavarropa)
        if type(xtipo) is int:
            if xtipo == 1:
                disp = self.cargaUnTelevisor()
                print('Se cargaron los datos de un televisor.')
            elif xtipo == 2:
                disp = self.cargaUnaHeladera()
                print('Se cargaron los datos de una heladera.')
            elif xtipo == 3:
                disp = self.cargaUnLavarropa()
                print('Se cargaron los datos de un lavarropa.')
            else:
                print('Parametro xtipo incorrecto. Debe ser int. No se carga nada.')
        print('----------------------------------')
        return disp

    def agregarElemento(self,unAparato): ### Con interface, (Inciso 2)
        self.__listaAparatos.agregarAparato(unAparato)
        print('Se agrego el aparato.')

    def insertarElemento(self,unAparato,xpos): ### Carga un dispositivo en una posicion determinada (Inciso 1)
        if type(xpos) is int:
            self.__listaAparatos.insertaAparato(unAparato,xpos - 1)

    def mostrarElemento(self,xpos): ### Con interface, (Inciso 3)
        if type(xpos) is int:
            dato = self.__listaAparatos.buscaPosicion(xpos - 1)
            if dato != None:
                if isinstance(dato,Televisor):
                    print('En esta posicion hay un objeto de clase Televisor.')
                elif isinstance(dato,Heladera):
                    print('En esta posicion hay un objeto de clase Heladera.')
                elif isinstance(dato,Lavarropa):
                    print('En esta posicion hay un objeto de clase Lavarropa.')
            else:
                print('No se encontro un objeto en la lista con la posicion solicitada.')
        else:
            print('Error. La posicion debe ser de tipo entero.')

    def informaAparatosPhillips(self): ### Inciso 4
        arrecont = [0,0,0] ### Lista con contadores aparatos Phillips(primera componente televisores, segunda heladeras, tercera lavarropas)
        for aparato in self.__listaAparatos:
            if isinstance(aparato,Televisor):
                if aparato.getMarca() == 'Phillips':
                    arrecont[0] += 1
            elif isinstance(aparato,Heladera):
                if aparato.getMarca() == 'Phillips':
                    arrecont[1] += 1
            elif isinstance(aparato,Lavarropa):
                if aparato.getMarca() == 'Phillips':
                    arrecont[2] += 1
        print('Cantidad de aparatos de marca Phillips.')
        print('----------------------------------')
        print('Televisores: {}'.format(arrecont[0]))
        print('Heladeras: {}'.format(arrecont[1]))
        print('Lavarropas: {}'.format(arrecont[2]))

    def MarcaLavarropasCargaSup(self):
        print('Marcas disponibles de lavarropas que tienen carga superior')
        for aparato in self.__listaAparatos:
            if isinstance(aparato,Lavarropa):
                if aparato.getTipoCarga() == 'superior':
                    print(aparato.getMarca())

    def calculaImporte(self,unAparato): ### Calcula importe segun el tipo de aparato
        importe = unAparato.getPrecioBase() ### Primero se obtiene el precio base
        if isinstance(unAparato,Televisor):
            if unAparato.getTipoDefinicion() == 'SD':
                importe += ((1 * importe) / 100) ### Suma porcentaje 1%
            elif unAparato.getTipoDefinicion() == 'HD':
                importe += ((2 * importe) / 100) ### Suma porcentaje 2%
            elif unAparato.getTipoDefinicion() == 'FULL HD':
                importe += ((3 * importe) / 100)  ### Suma porcentaje 3%
            if unAparato.getConexionInternet(): ### True (tiene conexion a internet)
                importe += ((10 * importe) / 100) ### Suma porcentaje 10%


        if isinstance(unAparato,Heladera):
            if unAparato.getFreezer(): ### True (tiene Freezer)
                importe += ((5 * importe) / 100)  ### Suma porcentaje 5%
            else: ### False (no tiene freezer)
                importe += ((1 * importe) / 100)  ### Suma porcentaje 1%
            if unAparato.getCiclica(): ### True (es ciclica)
                importe += ((10 * importe) / 100)  ### Suma porcentaje 10%

        if isinstance(unAparato,Lavarropa):
            if unAparato.getCapacidadLavado() <= 5:
                importe += ((1 * importe) / 100)  ### Suma porcentaje 1%
            elif unAparato.getCapacidadLavado() > 5:
                importe += ((3 * importe) / 100)  ### Suma porcentaje 3%

        return importe

    def MuestraAparatos(self): ### Inciso 6
        print('Aparatos a la venta.')
        print('----------------------------------')
        for aparato in self.__listaAparatos:
            if isinstance(aparato,Televisor):
                print('Tipo de aparato: Televisor.')
            elif isinstance(aparato,Heladera):
                print('Tipo de aparato: Heladera.')
            elif isinstance(aparato,Lavarropa):
                print('Tipo de aparato: Lavarropa.')
            print(aparato)
            print('Importe: $%.2f' % (self.calculaImporte(aparato)))
            print('----------------------------------')

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[aparato.toJSON() for aparato in self.__listaAparatos]
        )
        return d