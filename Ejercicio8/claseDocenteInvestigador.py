from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoriaincentivos = ''
    __importeextra = 0.0

    def __init__(self,cuil, apellido, nombre, sueldobasico, antiguedad, carrera='', cargo='', catedra='', area='', tipoinvestigacion='', categoriaincentivos='', importeextra=0, categoria=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, area, tipoinvestigacion, categoriaincentivos, importeextra, categoria)
        Investigador.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,area,tipoinvestigacion) ### Atributos clase investigador
        self.__categoriaincentivos = categoriaincentivos
        if type(importeextra) is float:
            self.__importeextra = importeextra
        else:
            print('Error de parametro importe extra en DocenteInvestigador.')

    def getCategoriaIncentivos(self):
        return self.__categoriaincentivos

    def getImporteExtra(self):
        return self.__importeextra

    def calculaSueldo(self):
        total = Docente.calculaSueldo(self) + self.__importeextra
        return total

    def setImporteExtra(self, nuevoImporteExtra):
        if type(nuevoImporteExtra) is float:
            self.__importeextra = nuevoImporteExtra
            print('Se ha modificado el importe extra de este docente investigador.')
            print('Nuevo importe extra: $%.2f' % (self.__importeextra))
        else:
            print('Error de parametro nuevoImporteExtra. Debe ser float.')

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(), ### Atributos de personal
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldobasico=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                carrera=super().getCarrera(), ### Atributos de docente
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                area=super().getArea(),  ### Atributos de investigador
                tipoinvestigacion=super().getTipoInvestigacion(),
                categoriaincentivos=self.__categoriaincentivos, ### Atributos propios
                importeextra=self.__importeextra
            )
        )
        return d