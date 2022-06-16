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

        ### Porcentajes por cargo
        self.__porcensimple = 10  ### Porcentaje por cargo simple (10% por defecto)
        self.__porcensemiex = 20  ### Porcentaje por cargo semiexclusivo (20% por defecto)
        self.__porcenexclu = 50  ### Porcentaje por cargo exclusivo (50% por defecto)

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
            porcentajecargo = ((super().getSueldoBasico() * self.__porcensimple) / 100)  ### Porcentaje por cargo simple
        elif self.__cargo == 'semiexclusivo':
            porcentajecargo = ((super().getSueldoBasico() * self.__porcensemiex) / 100)  ### Porcentaje por cargo semiexclusivo
        elif self.__cargo == 'exclusivo':
            porcentajecargo = ((super().getSueldoBasico() * self.__porcenexclu) / 100) ### Porcentaje por cargo exclusivo
        total = super().getSueldoBasico() + porcentantiguedad + porcentajecargo
        return total

    def setPorcentajeporCargo(self,nuevoPorcentaje):
        if type(nuevoPorcentaje) is int:
            if self.__cargo == 'simple':
                print('Este docente tiene cargo simple.')
                self.__porcensimple = nuevoPorcentaje
                print('Se ha modificado el porcentaje para cargo simple de este docente.')
                print('Nuevo porcentaje: {}'.format(self.__porcensimple))
            elif self.__cargo == 'semiexclusivo':
                print('Este docente tiene cargo semiexclusivo.')
                self.__porcensemiex = nuevoPorcentaje
                print('Se ha modificado el porcentaje para cargo semiexlusivo de este docente.')
                print('Nuevo porcentaje: {}'.format(self.__porcensemiex))
            elif self.__cargo == 'exclusivo':
                print('Este docente tiene cargo exclusivo.')
                self.__porcenexclu = nuevoPorcentaje
                print('Se ha modificado el porcentaje para cargo exlusivo de este docente.')
                print('Nuevo porcentaje: {}'.format(self.__porcenexclu))
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
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d