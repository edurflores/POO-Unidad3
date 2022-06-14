from clasePersonal import Personal

class Apoyo(Personal): ### Personal de apoyo
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria=0, carrera='', cargo='', catedra='', area='', tipoinvestigacion='', categoriaincentivos='', importeextra=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, categoria, area, tipoinvestigacion, categoriaincentivos, importeextra)
        if type(categoria) is int:
            self.__categoria = categoria
        else:
            print('Error de parametro categoria en Apoyo. Debe ser int.')

    def calculaSueldo(self):
        porcentantiguedad = ((super().getSueldoBasico() * super().getAntiguedad()) / 100)  ### Porcentaje por antiguedad
        porcentajecat = 0
        if self.__categoria >= 1 and self.__categoria <= 10:
            porcentajecat = ((super().getSueldoBasico() * 10) / 100) ### Porcentaje por categoria de 1 a 10, 10%
        elif self.__categoria >= 11 and self.__categoria <= 20:
            porcentajecat = ((super().getSueldoBasico() * 20) / 100) ### Porcentaje por categoria de 11 a 20, 20%
        elif self.__categoria >= 21 and self.__categoria <= 22:
            porcentajecat = ((super().getSueldoBasico() * 30) / 100) ### Porcentaje por categoria de 21 a 22, 30%
        total = super().getSueldoBasico() + porcentantiguedad + porcentajecat
        return total


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

