from claseAparato import Aparato

class Lavarropa(Aparato):
    __capacidadlavado = 0 ## en kg entero
    __velocidadcentri = 0 ## en rpm entero
    __cantidadprogramas = 0
    __tipocarga = ''

    def __init__(self,marca,modelo,color,paisfabric,preciobase,capacidadLavado,velocidadcentri,cantidadprogramas,tipocarga):
        super().__init__(marca,modelo,color,paisfabric,preciobase)
        if type(capacidadLavado) is int:
            self.__capacidadlavado = capacidadLavado
        else:
            print('Error de parametro capacidad de lavado en Lavarropa. Debe ser int.')
        if type(velocidadcentri) is int:
            self.__velocidadcentri = velocidadcentri
        else:
            print('Error de parametro velocidad de centrifugado en Lavarropa. Debe ser int.')
        if type(cantidadprogramas) is int:
            self.__cantidadprogramas = cantidadprogramas
        else:
            print('Error de parametro cantidad de programas en Lavarropa. Debe ser int.')
        self.__tipocarga = tipocarga

    def getTipoCarga(self):
        return self.__tipocarga

    def getCapacidadLavado(self):
        return self.__capacidadlavado

    def toJSON(self): ### Aparentemente los atributos heredados tambien se ponen como self y no super en este caso.
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getMarca(),
                modelo=self.getModelo(),
                color=self.getColor(),
                paisfabric=self.getPaisFabric(),
                preciobase=self.getPrecioBase(),
                capacidadLavado=self.__capacidadlavado,
                velocidadcentri=self.__velocidadcentri,
                cantidadprogramas=self.__cantidadprogramas,
                tipocarga=self.__tipocarga
            )
        )
        return d