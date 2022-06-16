from clasePersonal import Personal

class Apoyo(Personal): ### Personal de apoyo
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria=0, carrera='', cargo='', catedra='', area='', tipoinvestigacion='', categoriaincentivos='', importeextra=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, categoria, area, tipoinvestigacion, categoriaincentivos, importeextra)
        if type(categoria) is int:
            self.__categoria = categoria
        else:
            print('Error de parametro categoria en Apoyo. Debe ser int.')

        ### Porcentajes por categoria
        self.__porcencatcatUno = 10 ### Porcentaje por categoria de 1 a 10, (por defecto 10%)
        self.__porcencatcatDos = 20 ### Porcentaje por categoria de 11 a 20, (por defecto 20%)
        self.__porcencatcatTres = 30 ### Porcentaje por categoria de 21 a 22, (por defecto 30%)

    def calculaSueldo(self):
        porcentantiguedad = ((super().getSueldoBasico() * super().getAntiguedad()) / 100)  ### Porcentaje por antiguedad
        porcentajecat = 0
        if self.__categoria >= 1 and self.__categoria <= 10:
            porcentajecat = ((super().getSueldoBasico() * self.__porcencatcatUno) / 100) ### Porcentaje por categoria de 1 a 10, 10%
        elif self.__categoria >= 11 and self.__categoria <= 20:
            porcentajecat = ((super().getSueldoBasico() * self.__porcencatcatDos) / 100) ### Porcentaje por categoria de 11 a 20, 20%
        elif self.__categoria >= 21 and self.__categoria <= 22:
            porcentajecat = ((super().getSueldoBasico() * self.__porcencatcatTres) / 100) ### Porcentaje por categoria de 21 a 22, 30%
        total = super().getSueldoBasico() + porcentantiguedad + porcentajecat
        return total

    def setPorcentajeporCategoria(self, nuevoPorcentaje):
        if type(nuevoPorcentaje) is int:
            if self.__categoria >= 1 and self.__categoria <= 10 == 'simple':
                print('Este agente es personal de apoyo en categoria de 1 a 10.')
                self.__porcencatcatUno = nuevoPorcentaje
                print('Se ha modificado el porcentaje para la categoria de 1 a 10 de este agente.')
                print('Nuevo porcentaje: {}'.format(self.__porcencatcatUno))
            elif self.__categoria >= 11 and self.__categoria <= 20:
                print('Este agente es personal de apoyo en categoria de 11 a 20.')
                self.__porcencatcatDos = nuevoPorcentaje
                print('Se ha modificado el porcentaje para la categoria de 11 a 20 de este agente.')
                print('Nuevo porcentaje: {}'.format(self.__porcencatcatDos))
            elif self.__categoria >= 21 and self.__categoria <= 22:
                print('Este agente es personal de apoyo en categoria de 21 a 22.')
                self.__porcencatcatTres = nuevoPorcentaje
                print('Se ha modificado el porcentaje para la categoria de 21 a 22 de este agente')
                print('Nuevo porcentaje: {}'.format(self.__porcencatcatTres))
        else:
            print('Error de parametro nuevoPorcentaje. Debe ser int.')

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldobasico=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                categoria=self.__categoria
            )
        )
        return d

