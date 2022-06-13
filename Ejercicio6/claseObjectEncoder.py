import json
from pathlib import Path
from claseManejadorAparatos import ManejadorAparatos
from claseAparato import Aparato
from claseTelevisor import Televisor
from claseHeladera import Heladera
from claseLavarropa import Lavarropa

class ObjectEncoder:

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
        if class_name == 'ManejadorAparatos': ### Nombre del manejador usado
            aparatos = d['aparatos']
            dAparatos = aparatos[0]
            manejador = class_() ### Sera de clase ManejadorAparatos
            for i in range(len(aparatos)):
                dAparatos = aparatos[i]
                class_name = dAparatos.pop('__class__')
                class_ = eval(class_name)
                atributos = dAparatos['__atributos__']
                unAparato = class_(**atributos)
                manejador.agregaUnAparato(unAparato)
        return manejador

    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open('w',encoding='UTF-8') as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self,texto):
        return json.loads(texto)