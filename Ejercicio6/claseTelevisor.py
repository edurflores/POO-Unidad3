from claseAparato import Aparato

class Televisor(Aparato):
    __tipopantalla = ''
    __pulgadas = ''
    __tipodefinicion = ''
    __conexioninternet = bool ### booleano

    def __init__(self,marca,modelo,color,paisfabric,preciobase,tipopantalla,pulgadas,tipodefinicion,conexioninternet):
        super().__init__(marca,modelo,color,paisfabric,preciobase)
        self.__tipopantalla = tipopantalla
        self.__pulgadas = pulgadas
        self.__tipodefinicion = tipodefinicion
        if type(conexioninternet) is bool:
            self.__conexioninternet = conexioninternet
        else:
            print('Error de parametro conexion en Televisor. Debe ser booleano.')

    def getTipoPantalla(self):
        return self.__tipopantalla

    def getTipoDefinicion(self):
        return self.__tipodefinicion

    def getConexionInternet(self):
        return self.__conexioninternet

    def toJSON(self): ### Herencia: para usar atributos de la clase padre no queda otra que con metodos get.
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getMarca(),
                modelo=self.getModelo(),
                color=self.getColor(),
                paisfabric=self.getPaisFabric(),
                preciobase=self.getPrecioBase(),
                tipopantalla=self.__tipopantalla,
                pulgadas=self.__pulgadas,
                tipodefinicion=self.__tipodefinicion,
                conexioninternet=self.__conexioninternet
            )
        )
        return d