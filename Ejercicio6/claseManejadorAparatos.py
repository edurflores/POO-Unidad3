import csv
from claseAparato import Aparato
from claseTelevisor import Televisor
from claseHeladera import Heladera
from claseLavarropa import Lavarropa

from claseLista import Lista

class ManejadorAparatos:
    __listaAparatos = None

    def __init__(self):
        self.__listaAparatos = Lista()

    def testTelevisores(self):
        archivo = open('televisores.csv')
        reader = csv.reader(archivo,delimiter=';')
        ban = True
        if ban:
            ban = not ban
        else:
            for fila in reader:
                untele = Televisor(fila[0],fila[1],fila[2],fila[3],float(fila[4]),fila[5],fila[6],fila[7],bool(fila[8]))
                self.__listaAparatos.agregarAparato(untele)
        archivo.close()
        print('Se han cargado televisores para testeo.')

    def cargaUnTelevisor(self):
        print('Ingrese los datos del televisor.')
        print('----------------------------------')
        marc = input('Ingrese marca: ')
        mod = input('Ingrese modelo: ')
        col = input('Ingrese color: ')
        pais = input('Ingrese pais de fabricacion: ')
        precio = float(input('Ingrese precio base: '))
        tipopant = input('Ingrese tipo de pantalla (CRT, VGA, SVGA, Plasma, LCD, LED, TouchScreen, MultiTouch): ')
        pulg = int(input('Ingrese cantidad de pulgadas (numero entero): '))
        tdef = input('Ingrese tipo de definicion (SD, HD, FULL HD): ')
        conex = input('Indique si tiene conexion a internet (1- Si. 2- No.): ')
        if conex == '1':
            conex = True
        else:
            conex = False
        unTelevisor = Televisor(marc,mod,col,pais,precio,tipopant,pulg,tdef,conex)
        return unTelevisor

    def cargaUnaHeladera(self):
        print('Ingrese los datos de la heladera.')
        print('----------------------------------')
        marc = input('Ingrese marca: ')
        mod = input('Ingrese modelo: ')
        col = input('Ingrese color: ')
        pais = input('Ingrese pais de fabricacion: ')
        precio = float(input('Ingrese precio base: '))
        cap = int(input('Ingrese capacidad en litros (numero entero): '))
        frez = input('Indique si tiene freezer (1- Si. 2- No.): ')
        if frez == '1':
            frez = True
        else:
            frez = False
        cic = input('Indique si es ciclica (1- Si. 2- No.): ')
        if cic == '1':
            cic = True
        else:
            cic = False
        unaHeladera = Heladera(marc,mod,col,pais,precio,cap,frez,cic)
        return unaHeladera

    def cargaUnLavarropa(self):
        print('Ingrese los datos del lavarropa.')
        print('----------------------------------')
        marc = input('Ingrese marca: ')
        mod = input('Ingrese modelo: ')
        col = input('Ingrese color: ')
        pais = input('Ingrese pais de fabricacion: ')
        precio = float(input('Ingrese precio base: '))
        caplav = int(input('Ingrese capacidad de lavado kg (numero entero): '))
        vel = int(input('Ingrese velocidad de centrifugado rpm (numero entero): '))
        cantpr = int(input('Ingrese cantidad de programas (numero entero): '))
        tipocar = input('Ingrese tipo de carga (Frontal, Superior): ')
        unLavarropa = Lavarropa(marc,mod,col,pais,precio,caplav,vel,cantpr,tipocar)
        return unLavarropa

    def cargaUnDispositivo(self,xtipo):
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
                print('Valor incorrecto. No se carga nada.')
        print('----------------------------------')
        return disp

    def agregaUnAparato(self,unAparato):
        self.__listaAparatos.agregarAparato(unAparato)
        print('Se agrego el aparato.')

    def insertaAparatoPosicion(self,unAparato,xpos):
        if type(xpos) is int:
            self.__listaAparatos.insertaAparato()

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
                if aparato.getTipoCarga() == 'Superior':
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
            if unAparato.getConexionInternet(): ### True
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
            print('Importe: {}'.format(self.calculaImporte(aparato)))
            print('----------------------------------')