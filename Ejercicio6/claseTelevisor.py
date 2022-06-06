from claseAparato import Aparato

class Televisor(Aparato):
    __tipopantalla = ''
    __pulgadas = ''
    __tipodefinicion = ''
    __conexioninternet = '' ### booleano

    def __init__(self,marc,mod,col,pais,precio,tipopant,pulg,tipodef,conex):
        super().__init__(marc,mod,col,pais,precio)
        self.__tipopantalla = tipopant
        self.__pulgadas = pulg
        self.__tipodefinicion = tipodef
        if type(conex) is bool:
            self.__conexioninternet = conex
        else:
            print('Error de parametro conexion en Televisor. Debe ser booleano.')

    def getTipoPantalla(self):
        return self.__tipopantalla

    def getTipoDefinicion(self):
        return self.__tipodefinicion

    def getConexionInternet(self):
        return self.__conexioninternet