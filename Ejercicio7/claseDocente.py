from clasePersonal import Personal

class Docente(Personal):
    __carrera = '' ### carrera en la que dicta clases
    __cargo = '' ## jefe de catedra, jtp, etc.
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera='', cargo='', catedra='', categoria=0, area='', tipoinvestigacion='', categoriaincentivos='', importeextra=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, categoria, area, tipoinvestigacion, categoriaincentivos, importeextra)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def calculaSueldo(self):
        porcentantiguedad = ((super().getSueldoBasico() * super().getAntiguedad()) / 100) ### Porcentaje por antiguedad
        porcentajecargo = 0
        if self.__cargo == 'simple':
            porcentajecargo = ((super().getSueldoBasico() * 10) / 100)  ### Porcentaje por cargo simple 10%
        elif self.__cargo == 'semiexclusivo':
            porcentajecargo = ((super().getSueldoBasico() * 20) / 100)  ### Porcentaje por cargo semiexclusivo 20%
        elif self.__cargo == 'exclusivo':
            porcentajecargo = ((super().getSueldoBasico() * 50) / 100) ### Porcentaje por cargo semiexclusivo 50%
        total = super().getSueldoBasico() + porcentantiguedad + porcentajecargo
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
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d