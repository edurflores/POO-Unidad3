from claseAparato import Aparato

class Lavarropa(Aparato):
    __capacidadlavado = 0 ## en kg entero
    __velocidadcentri = 0 ## en rpm entero
    __cantidadprogramas = 0
    __tipocarga = ''

    def __init__(self,marc,mod,col,pais,precio,caplav,vel,cantprog,tipoc):
        super().__init__(marc,mod,col,pais,precio)
        if type(caplav) is int:
            self.__capacidadlavado = caplav
        else:
            print('Error de parametro capacidad de lavado en Lavarropa. Debe ser int.')
        if type(vel) is int:
            self.__velocidadcentri = vel
        else:
            print('Error de parametro velocidad de centrifugado en Lavarropa. Debe ser int.')
        if type(cantprog) is int:
            self.__cantidadprogramas = cantprog
        else:
            print('Error de parametro cantidad de programas en Lavarropa. Debe ser int.')
        self.__tipocarga = tipoc

    def getTipoCarga(self):
        return self.__tipocarga

    def getCapacidadLavado(self):
        return self.__capacidadlavado

