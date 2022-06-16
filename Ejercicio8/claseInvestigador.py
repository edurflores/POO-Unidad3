from clasePersonal import Personal

class Investigador(Personal):
    __area = ''
    __tipoinvestigacion = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, area='', tipoinvestigacion='', carrera='', cargo='', catedra='', categoria=0, categoriaincentivos='', importeextra=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, categoria, area, tipoinvestigacion, categoriaincentivos, importeextra)
        self.__area = area
        self.__tipoinvestigacion = tipoinvestigacion

    def getArea(self):
        return self.__area

    def getTipoInvestigacion(self):
        return self.__tipoinvestigacion

    def calculaSueldo(self):
        porcentantiguedad = ((super().getSueldoBasico() * super().getAntiguedad()) / 100)  ### Porcentaje por antiguedad
        total = super().getSueldoBasico() + porcentantiguedad ### Sueldo basico + porcentaje por antiguedad
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
                area=self.__area,
                tipoinvestigacion=self.__tipoinvestigacion
            )
        )
        return d

